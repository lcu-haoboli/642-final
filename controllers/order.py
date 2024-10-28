from flask import render_template, request, redirect, url_for,Blueprint,json, session,flash
from base import Session
from models.Order import Order
from models.Payment import Payment
from models.Payment import CreditCardPayment
from models.Payment import DebitCardPayment
from models.OrderLine import OrderLine
from datetime import date
db_session = Session()

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
			return orders
		except Exception as e:
			print(e)
			flash("Internal Error happend:" + e)
	else:
		flash("You dont have access to this function")
		return redirect(url_for("home"))
	

	





	# query db
