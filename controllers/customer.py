from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template

customer_bp = Blueprint("customer", __name__, static_folder="static", template_folder="templates/products")

@customer_bp.route("/customer")
def customer():
	return render_template("customer.html")