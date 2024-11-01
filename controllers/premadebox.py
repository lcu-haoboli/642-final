from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template
from base import Session
from models.Veggie import Veggie
premadebox_bp = Blueprint("premadebox", __name__, static_folder="static", template_folder="templates/products")


db_session = Session()
@premadebox_bp.route("/")
def premadebox():
	try:
		if session.get("userType") == "staff":
			flash("Please login in as Customer", "info")
		print(session)
		url_boxsize = request.args.get('boxsize')
		if url_boxsize != None:
			session["boxsize"] = url_boxsize
		elif session.get("boxsize") == None:	  
			session["boxsize"] = 'all'
		# keep the box size gloal
		veggies = db_session.query(Veggie).all()
		itemInBox = session.get("itemInBox") if session.get("itemInBox") != None else []
		print(session)
		return render_template("products/premadebox.html", veggies = veggies,  boxsize = session["boxsize"], itemInBox = itemInBox)
	except Exception as e:
		print(e)
		return render_template("products/premadebox.html", veggies = [], boxsize = session["boxsize"])
	

@premadebox_bp.route("/selectbox", methods = ["POST"])
def selectBox():
	try:
		if session.get("userId") == None or session.get("logged_in") != True:
			return redirect(url_for("login.login"))
		if session.get("userType") == "staff":
			return redirect(url_for("premadebox.premadebox"))
		selected_boxsize = request.form.get("premadeBoxSize")
		print(selected_boxsize)
		# reselct box size will clean up the selected item in the current box
		if selected_boxsize != session["boxsize"]:
			session["itemInBox"] = []
			session["premadebox"] = None
			session["boxsize"] = selected_boxsize
		return redirect(url_for("premadebox.premadebox", boxsize = session["boxsize"]))
	except Exception as e:
		print(e)
		flash("Erro", 'error')
		return redirect(url_for("premadebox.premadebox", boxsize = 'all'))

@premadebox_bp.route("/addtobox/<veggieId>", methods = ["POST"])
def addToBox(veggieId):
	try:
		if session.get("userType") == "staff":
			return redirect(url_for("premadebox.premadebox"))
		if session.get("userId") == None or session.get("logged_in") != True:
			return redirect(url_for("login.login"))
		quantity = request.form.get("quantity-input")
		veggieName = request.form.get("veggie-name")
		itemInBox = session.get("itemInBox")
		boxsize = session.get("boxsize")
		if  boxsize == 'all':
			flash("You Must Select a Premade Box first before Adding veggie","warning")
			return redirect(url_for("premadebox.premadebox"))
		if quantity == None or quantity == '':
			flash("You Must Add quantity before adding to PremadeBox","warning")
			return redirect(url_for("premadebox.premadebox"))
		itemObj = {
				"veggie" : int(veggieId),
				"veggieName": veggieName,
				"quantity" : int(quantity),
				"boxSize" : boxsize
			}
		itemInBox.append(itemObj)
		session["premadebox"] = itemInBox
		return redirect(url_for("premadebox.premadebox", boxsize = boxsize))
	except Exception as e:
		print(e)
		return redirect(url_for("premadebox.premadebox", boxsize = boxsize))

@premadebox_bp.route("/addtocheckout", methods = ["POST"])
def addToCheckOut():
	return redirect(url_for("cart.cart"))