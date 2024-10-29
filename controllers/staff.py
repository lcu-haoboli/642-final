from flask import Blueprint, flash, redirect, url_for, jsonify,request,render_template,session
from base import Session
from models.Order import Order
from models.Person import Person
from models.Payment import Payment
from models.Payment import CreditCardPayment
from models.Payment import DebitCardPayment
from models.OrderLine import OrderLine
from models.CorporateCustomer import CorporateCustomer
from datetime import date
from models.Customer import Customer
from sqlalchemy.sql import text
db_session = Session()


staff_bp = Blueprint("staff", __name__, static_folder="static", template_folder="templates/staff")

@staff_bp.route("/")
def dashboard():
	if session["userType"] != "staff" or session['logged_in'] != True:
		return redirect(url_for("login.login"))
	return render_template("staff/dashboard.html")
	

@staff_bp.route("/all_customers")
def allCustomer():
	# query db
	query = text("select c.*, p.* from customer c left join person p on c.custId = p.id")
	result = db_session.execute(query).all()
	cust_info = []
	if result:
		for cust in result:
			custInfo = {
					"id" : cust[0],
					"address" : cust[1],
					"custBalance" : cust[2],
					"maxOwning" : cust[3],
					"firstname" : cust[5],
					"lastname" : cust[6],
					"username" : cust[8]
					}
			cust_info.append(custInfo)
	return render_template("staff/all_customers.html", customers = cust_info)

@staff_bp.route("/all_orders")
def allOrder():
	try:
		orders_custs = db_session.query(Order,Customer).join(Customer).all()
		orders_corp = db_session.query(Order,CorporateCustomer).join(CorporateCustomer).all()
		list_orders_custs = []
		for order_cust in orders_custs:
			order = order_cust[0].__dict__
			cust = order_cust[1].__dict__
			list_orders_custs.append({**order, **cust})
		print(list_orders_custs)
		for item in list_orders_custs:
			print(item)
		return render_template("staff/all_orders.html", orders = list_orders_custs)
	except Exception as e:
		flash(str(e), "error")
		return render_template("staff/all_orders.html", orders = [])
		

	