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
from sqlalchemy.sql import text, alias
db_session = Session()
person_alias = alias(Person)

staff_bp = Blueprint("staff", __name__, static_folder="static", template_folder="templates/staff")

@staff_bp.route("/")
def dashboard():
	if session["userType"] != "staff" or session['logged_in'] != True:
		return redirect(url_for("login.login"))
	return render_template("staff/dashboard.html")
	

@staff_bp.route("/all_customers")
def allCustomer():
	# query db
	try:
		customers = db_session.query(Customer).all()
		corp_cust = db_session.query(CorporateCustomer).all()
		return render_template("staff/all_customers.html", customers = customers, corp_cust = corp_cust)
	except Exception as e:
		pass

@staff_bp.route("/all_orders/<type>")
def allOrder(type):
	print(type)
	cust_orders = []
	corp_cust_order = []
	try:
		# normal customer
		current_order_cust_data = (db_session.query(Order, Customer)
			.join(Person, Order.orderCustomer == Person.id)
			.join(Customer, Customer.custId == Person.id)
			.filter(Order.orderStatus != "delivered" and Order.orderStatus != "canceled" )
			.all())
		current_cust_orders = merge_cust_order_data(current_order_cust_data)

		prev_order_cust_data = (db_session.query(Order, Customer)
			.join(Person, Order.orderCustomer == Person.id)
			.join(Customer, Customer.custId == Person.id)
			.filter(Order.orderStatus == "delivered" or Order.orderStatus == "canceled" )
			.all())
		prev_cust_orders = merge_cust_order_data(prev_order_cust_data)

		# corperate customer
			
		db_session.flush()
		db_session.commit()
		current_orders_corp_data = (db_session.query(Order, CorporateCustomer)
				 .join(Person, Order.orderCustomer == Person.id)
				 .join(CorporateCustomer,CorporateCustomer.corpCustId == Person.id)
				 .filter(Person.userType == "corporateCustomer")
				 .filter(Order.orderStatus != "delivered" and Order.orderStatus != "canceled" )
				 .all()
				 )
		current_corp_cust_order = merge_corp_order_data(current_orders_corp_data)

		prev_orders_corp_data = (db_session.query(Order, CorporateCustomer)
				 .join(Person, Order.orderCustomer == Person.id)
				 .join(CorporateCustomer,CorporateCustomer.corpCustId == Person.id)
				 .filter(Person.userType == "corporateCustomer")
				 .filter(Order.orderStatus == "delivered" or Order.orderStatus == "canceled" )
				 .all()
				 )
		prev_corp_cust_order = merge_corp_order_data(prev_orders_corp_data)

		if type == "current":
			cust_orders = current_cust_orders
			corp_cust_order = current_corp_cust_order

		elif type == "previous":
			cust_orders = prev_cust_orders
			corp_cust_order =prev_corp_cust_order
			


		return render_template("staff/all_orders.html", cust_orders = cust_orders, corp_cust_order = corp_cust_order,type = type)
	except Exception as e:
		flash(str(e), "error")
		return render_template("staff/all_orders.html", orders = [])
		


def merge_cust_order_data(datas):
	merge_data = []
	if len(datas) > 0:
		for order, customer in datas:
			merge_record = {
				"firstName" : customer.firstName,
				"lastName" : customer.lastName,
				"userName" : customer.userName,
				"userType" : customer.userType,
				"orderId" : order.orderId,
				"orderDate" : order.orderDate,
				"orderStatus" : order.orderStatus,
				"customerId": customer.custId,
				"custAddress" : customer.custAddress,
				"custBalance" : customer.custBalance,
				"maxOwning" : customer.maxOwning
			}
			merge_data.append(merge_record)
	return merge_data

def merge_corp_order_data(datas):
	merge_data = []
	if len(datas) > 0:
		for order, corporateCustomer in datas:
			merge_record = {
				"firstName" : corporateCustomer.firstName,
				"lastName" : corporateCustomer.lastName,
				"userName" : corporateCustomer.userName,
				"userType" : corporateCustomer.userType,
				"orderId" : order.orderId,
				"orderDate" : order.orderDate,
				"orderStatus" : order.orderStatus,
				"corpId": corporateCustomer.corpCustId,
				"discountRate" : corporateCustomer.discountRate,
				"maxCredit" : corporateCustomer.maxCredit,
				"minBalance" : corporateCustomer.minBalance 
			}
			merge_data.append(merge_record)
	return merge_data