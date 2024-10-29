from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template
from base import Session
from models.Person import Person
from models.Customer import Customer
from models.CorporateCustomer import CorporateCustomer

login_bp = Blueprint("login", __name__, static_folder="static", template_folder="templates")
db_session = Session()

@login_bp.route("/", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username_to_find = request.form['username']
		password_input = request.form['password']
		person = db_session.query(Person).filter_by(userName = username_to_find).first()
		if person != None:
			passwordInDB = person.password
			userType = person.userType
			isAuthenticated = isAuthenticatedUser(password_input, passwordInDB)
			if isAuthenticated:
				session["userId"] = person.id
				session['username'] = username_to_find
				session['logged_in'] = True
				session['userType'] = userType
				if userType == "customer":
					cust = db_session.query(Customer).filter(Customer.custId == person.id).first()
					session["maxOwning"] = cust.maxOwning
					session["custBalance"] = cust.custBalance
				if userType == "corporateCustomer":
					corp = db_session.query(CorporateCustomer).filter(CorporateCustomer.corpCustId == person.id).first()
					session["minBalance"] = corp.minBalance
					session["maxCredit"] = corp.maxCredit
				flash("Login successful!", "success")
				return redirect(url_for("home"))
			else:
				flash("Incorrect password. Please try again.", "error")
		else:
			flash("User not found. Please check your username.", "error")
	return render_template("login.html")

def isAuthenticatedUser(passwordInput, passwordInDB):
	return passwordInDB == passwordInput
	
