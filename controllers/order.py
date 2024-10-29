from flask import render_template, request, redirect, url_for,Blueprint,json, session,flash
from base import Session
from models.Order import Order
from models.Payment import Payment
from models.Veggie import Veggie
from models.Payment import CreditCardPayment
from models.Payment import DebitCardPayment
from models.Person import Person
from models.OrderLine import OrderLine
from datetime import date
db_session = Session()

order_bp = Blueprint("order",__name__, static_folder="static", template_folder="templates/order")
@order_bp.route("/customer/<id>")
def getOrdersByCustomerId(id):
	# check user role 
	currentUser = session.get("userId")
	if currentUser == None:
		return redirect(url_for("login.login"))
	
	# check is exist:
	currentUserType = session.get("userType")
	if currentUserType == "staff" or id == currentUser:
		try:
			orders = db_session.query(Order).filter_by(orderCustomer=id).all()
			print(orders)
			return render_template("order_by_cust_id.html")
		except Exception as e:
			print(e)
			flash("Internal Error happend:" + e)
	else:
		flash("You dont have access to this function")
		return redirect(url_for("home"))

@order_bp.route("/<id>")
def details(id):
	order_info = db_session.query(Order).filter(Order.orderId == id).first()
	order_cust = db_session.query(Person).filter(Person.id == order_info.orderCustomer).first()
	order_details_data = db_session.query(OrderLine, Veggie).filter(OrderLine.orderId == id).join(Veggie, Veggie.id == OrderLine.veggieId).all()
	order_details = []
	for detail in order_details_data:
		orderLine = detail[0].__dict__
		veggie = detail[1].__dict__
		order_details.append({**orderLine, **veggie})
	print(order_details)
	for item in order_details:
		print(item)
	return render_template("order/order_details.html", order = order_info, details = order_details , customer = order_cust)

	

	





	# query db
