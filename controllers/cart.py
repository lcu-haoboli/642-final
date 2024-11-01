from flask import render_template, request, redirect, url_for,Blueprint,json, session,flash
from base import Session
from models.Order import Order
from models.Payment import Payment
from models.Payment import CreditCardPayment
from models.Payment import DebitCardPayment
from models.OrderLine import OrderLine
from datetime import date
db_session = Session()

cart_bp = Blueprint("cart", __name__, static_folder="static", template_folder="templates")
@cart_bp.route('/', methods = ["GET", "POST"])
def cart():
    try:
        if session.get("logged_in") != True:
            flash("Login First!", "error")
            return redirect(url_for("login.login"))
        if session.get("userType") == "staff":
            flash("Please login as a customer!", "error")
            return redirect(url_for("login.login"))        
        cart_items = session.get('cartItems')
        maxCredit = session.get("maxCredit") 
        minBalance = session.get("minBalance")
        custBalance = session.get("custBalance")
        
        userType = session.get("userType")
        total_price = 0
        if cart_items:
            for item in cart_items:
                total_price += item["total"]
            session["total_amount_to_pay"] = total_price
            return render_template('cart.html', cart_items=cart_items, total_price=total_price, 
                                   maxCredit = maxCredit , owning = 0, minBalance=minBalance, 
                                   custBalance=custBalance, userType =userType,
                                   premadeBox = session.get("premadebox") if session.get("premadebox") else []
                                   )
        else: 
            session["total_amount_to_pay"] = total_price
            return render_template('cart.html', cart_items=[], total_price=0, 
                                   maxCredit = maxCredit , owning = 0, minBalance=minBalance, 
                                   custBalance=custBalance, userType =userType,
                                   premadeBox = session.get("premadebox") if session.get("premadebox") else [])
    except Exception as e:
        print("cart.cart", e)
        return render_template('cart.html', cart_items=[], total_price=0, 
                                   maxCredit = maxCredit , owning = 0, minBalance=minBalance, 
                                   custBalance=custBalance, userType =userType,
                                   premadeBox = [])




@cart_bp.route('/checkout', methods=['POST'])
def checkout():
    try:
        if session.get("userId") == None:
            flash("You need to Login first", "error")
            return redirect(url_for("login.login"))
        custId =  int(session["userId"])
        total_amount = session.get("total_amount_to_pay")
        today = date.today()
        order = Order(custId, today,"paid","normal" )
        db_session.add(order)
        db_session.flush()
        orderId = order.orderId


        payment_method = request.form.get("payment_method")
        card_expired_date = request.form.get("card_expired_date")
        bank_name = card_expired_date = request.form.get("bank_name")
        debit_card_number = card_expired_date = request.form.get("debit_card_number")
        # update payment table
        if payment_method == "credit_card":
            payment = CreditCardPayment(custId,orderId,total_amount,today,card_expired_date)
            
            db_session.add(payment)
        if payment_method == "debit_card":
            payment = DebitCardPayment(custId,orderId,total_amount,today,bank_name,debit_card_number)
            db_session.add(payment)
        
        # add order line:
        items = session.get("cartItems")
        if items:
            for item in items:
                orderLine = OrderLine(orderId,item["productId"],item["quantity"])
                db_session.add(orderLine)
            db_session.commit()

        premadeboxOrder = session.get("premadebox")
        if premadeboxOrder != None and premadeboxOrder != []:
            premadebox_order = Order(custId, today,"paid", "premadebox" )
            db_session.add(premadebox_order)
            db_session.flush()
            premadebox_order_id = premadebox_order.orderId
            if payment_method == "credit_card":
                payment = CreditCardPayment(custId,orderId,total_amount,today,card_expired_date)
                db_session.add(payment)
            if payment_method == "debit_card":
                payment = DebitCardPayment(custId,orderId,total_amount,today,bank_name,debit_card_number)
                db_session.add(payment)
            for item in premadeboxOrder:
                orderLine = OrderLine(premadebox_order_id,item["veggie"],item["quantity"])
                db_session.add(orderLine)
                print(item)
            # final commit the add order line
            db_session.flush()
            db_session.commit()
        
        # clean up
        if session.get("premadebox"):
            session.pop("premadebox")
        
        if session.get("cartItems"):
            session.pop("cartItems")
        flash(f"Made order successfuly", "success")
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
        flash(f"An error occurred while adding the category: {e}", "error")
        return redirect(url_for('cart.cart'))

