from flask import Blueprint, flash, redirect, url_for, jsonify, request,session,render_template

logout_bp = Blueprint("logout", __name__, static_folder="static", template_folder="templates")

@logout_bp.route("/")
def logout():
	return render_template("index.html")