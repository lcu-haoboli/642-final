from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template
from base import Session
from models.Person import Person

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
				session['username'] = username_to_find
				session['logged_in'] = True
				session['userType'] = userType
				return redirect(url_for("home"))
		return render_template("login.html", message= {"User Name Not Exist"})
	return render_template("login.html")

def isAuthenticatedUser(passwordInput, passwordInDB):
	return passwordInDB == passwordInput
	
