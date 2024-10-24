from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template

veggie_bp = Blueprint("veggie", __name__, static_folder="static", template_folder="templates/products")

@veggie_bp.route("/")
def veggie():
	return render_template("products/veggie.html")