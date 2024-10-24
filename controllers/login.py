from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template

login_bp = Blueprint("login", __name__, static_folder="static", template_folder="templates")

@login_bp.route("/")
def login():
	return render_template("login.html")