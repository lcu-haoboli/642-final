from flask import Flask,session,redirect,url_for,render_template,request
from models.database import  init_db
from controllers.veggie import veggie_bp
from controllers.staff import staff_bp
from controllers.customer import customer_bp
from controllers.login import login_bp
from controllers.premadebox import premadebox_bp
from controllers.logout import logout_bp
from controllers.cart import cart_bp
from controllers.order import order_bp



app = Flask(__name__)
app.secret_key = "gemini"
app.register_blueprint(veggie_bp, url_prefix="/veggie")
app.register_blueprint(staff_bp, url_prefix="/staff")
app.register_blueprint(customer_bp, url_prefix="/customer")
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(premadebox_bp, url_prefix="/premadebox")
app.register_blueprint(logout_bp, url_prefix="/logout")
app.register_blueprint(cart_bp, url_prefix="/cart")
app.register_blueprint(order_bp, url_prefix="/order")

@app.route("/")
def home():
    return render_template("index.html")




if __name__ == "__main__":
    init_db()
    app.run()