from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template
from base import Session
from models.Veggie import Veggie
veggie_bp = Blueprint("veggie", __name__, static_folder="static", template_folder="templates/products")

db_session = Session()

@veggie_bp.route("/")
def veggie():
	# query all veggie
	veggies = db_session.query(Veggie).all()
	# for veggie in veggies:
		# print(veggie)
	return render_template("products/veggie.html", veggies=veggies)
	# return render_template("products/veggie.html", veggie=[])