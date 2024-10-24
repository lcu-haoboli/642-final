from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template

premadebox_bp = Blueprint("premadebox", __name__, static_folder="static", template_folder="templates/products")

@premadebox_bp.route("/")
def premadebox():
	return render_template("products/premadebox.html")