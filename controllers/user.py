from flask import Blueprint, flash, redirect, url_for, jsonify,request,render_template,session
from base import Session
from models.Order import Order
from models.Person import Person
from models.Payment import Payment
from models.Payment import CreditCardPayment
from models.Payment import DebitCardPayment
from models.OrderLine import OrderLine
from models.Staff import Staff
from datetime import date
from models.CorporateCustomer import CorporateCustomer
from models.Customer import Customer
from sqlalchemy.sql import text
db_session = Session()


user_bp = Blueprint("user", __name__, static_folder="static", template_folder="templates/user")

@user_bp.route("/")
def details():
	try:
		id = session.get("userId")
		userType = session.get("userType")
		person = db_session.query(Person).filter(Person.id == id).first()
		data = None
		order_date = None
		if userType != "staff":
			order_date = db_session.query(Order).filter(Order.orderCustomer == id).all()
		if userType == "staff":
			data = db_session.query(Staff).filter(Staff.staffId == id).first()
		elif userType == "customer":
			data = db_session.query(Customer).filter(Customer.custId == id).first()
		elif userType == "corporateCustomer":
			data = db_session.query(CorporateCustomer).filter(CorporateCustomer.corpCustId == id).first()
		return render_template("user/user_details.html", basic = person, data = data, userType = userType, orders= order_date)
	except Exception as e:
		print(e)
		return render_template("user/user_details.html", basic = None, data = None, order_date = None)
		