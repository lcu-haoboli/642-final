


1. https://haoboli.pythonanywhere.com/


2. login information :
+----+-----------+----------+----------+---------------+-------------------+
| id | firstName | lastName | password | userName      | userType          |
+----+-----------+----------+----------+---------------+-------------------+
|  1 | kevin     | li       | 1        | kevinli       | staff             |
|  2 | amy       | luo      | 1        | kevina        | staff             |
|  3 | kevinc    | lic      | 1        | kevinc        | customer          |
|  4 | veggie    | retail   | 1        | veggie-retail | corporateCustomer |
+----+-----------+----------+----------+---------------+-------------------+

3. How to connect to database and init data:
	- create a database table call `veggie_shop`
	- open `base.py` file
	- edit engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/veggie_shop",echo=True)
	- replace user : your root name
	- replace password : your password
	- after connect success,under project folder,in terminal, run `python app.py` to create table and inject data

4. how to recreate the database
	1. under project folder,in terminal, run `python app.py`