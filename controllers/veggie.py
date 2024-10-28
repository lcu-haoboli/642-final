from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template,session,json
from base import Session
from models.Veggie import Veggie
veggie_bp = Blueprint("veggie", __name__, static_folder="static", template_folder="templates/products")

db_session = Session()

@veggie_bp.route("/", methods = ["GET", "POST"])
def veggie():
	veggies = db_session.query(Veggie).all()
	if request.method == 'POST':
		data = request.get_json()
		cartItems = data["cartItems"]
		session['cartItems'] = json.loads(cartItems)
		print(session['cartItems'])
		return render_template("products/veggie.html", veggies=veggies)
	return render_template("products/veggie.html", veggies=veggies)
	