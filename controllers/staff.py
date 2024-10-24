from flask import Blueprint, flash, redirect, url_for, jsonify,request,render_template,session

staff_bp = Blueprint("staff", __name__, static_folder="static", template_folder="templates/staff")


@staff_bp.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
   return render_template("global/account_dashboard.html")

@staff_bp.route("/inventory_management")
def inventory_management():
   try:
      pass
   except Exception as e:
      print("@staff.route(/inventory_management): %s", e)
      return []
   return render_template("staff/inventory_management.html")

@staff_bp.route("/product_with_inventory", methods=["GET"])
def product_with_inventory():
   product = {
      "product_name": "",
      "product_description": "",
      "product_price": "",
      "product_image": "",
      "product_status": "",
      "product_inventory_id": "",
      "product_inventory": 0
   }
   try:
      product_id = request.args.get('product_id')
      cursor = getCursor()
      sql_query = get_product_with_inventory()
      cursor.execute(sql_query, (product_id, ))
      result = cursor.fetchone()
      product = {
         "product_name": result[0],
         "product_description": result[1],
         "product_price": result[2],
         "product_image": result[3],
         "product_status": result[4],
         "product_inventory_id": result[5],
         "product_inventory": result[6]
      }
      return product
   except Exception as e:
      print("staff/product_with_inventory : %e ",e)
      return product

@staff_bp.route("/update_product_inventory", methods=["POST"])
def update_product_inventory():
   try:
      inventory_id = request.json.get('inventory_id')
      new_inventory = request.json.get('new_inventory')
    #   cursor = getCursor()
    #   sql_query = update_product_inventory_query()
    #   cursor.execute(sql_query, (new_inventory, inventory_id))
    #   cursor.close()
      return jsonify({'message': 'Inventory Updated successfully'}), 200
   except Exception as e:
    #   cursor.close()
      print("@staff.route(/update_product_inventory): %s", e)
      return jsonify({'message': 'Inventory Updated Error'}), 400


