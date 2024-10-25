from sqlalchemy import create_engine
from . import Veggie
from . import Person
from .import Staff
from . import Customer
from base import Base, session
from datetime import date
from .Veggie import UnitPriceVeggie
from .Veggie import WeightedVeggie
from .Veggie import PackVeggie

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/veggie_shop",echo=True)


def init_db():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)

	# person = Person.Person()
	today =  date.today()
	staff = Staff.Staff("kevin", "li", "1234", "kevinli", "staff", 1, today, "hello-dep", "abcd",None, None)
	staff2 = Staff.Staff("amy", "luo", "1234", "kevinli", "staff", 2, today, "hello-dep", "abcd",None, None)
	cust =Customer.Customer("kevinb", "lib", "1234", "kevinli","customer",3, "address", 0,0)

	#  add veggie to DB :
	veggies = [
    UnitPriceVeggie("carrot", 1.5, 10),
    UnitPriceVeggie("potato", 2.0, 5),
    UnitPriceVeggie("onion", 0.5, 20),
    UnitPriceVeggie("lettuce", 2.5, 1),
    UnitPriceVeggie("spinach", 3.0, 1),
    UnitPriceVeggie("bell pepper", 1.0, 5),
    WeightedVeggie("zucchini", 0.25, 2.0),
    WeightedVeggie("tomato", 0.5, 4.0),
    WeightedVeggie("cucumber", 1.0, 3.5),
    WeightedVeggie("broccoli", 0.75, 5.0),
	PackVeggie("kale", 1, 4.5),
    PackVeggie("asparagus", 1, 8.0),
    PackVeggie("fennel", 1, 5.0),
    PackVeggie("artichoke", 2, 6.5),
    PackVeggie("radish", 5, 4.0),
    PackVeggie("beetroot", 3, 6.0),
    PackVeggie("pumpkins", 1, 7.0),
    PackVeggie("eggplant", 2, 5.5),
    PackVeggie("bok choy", 3, 6.5),
    PackVeggie("green beans", 1, 4.0)
	]
	for veggie in veggies:
		session.add(veggie)
	session.add(staff)
	session.add(staff2)
	session.add(cust)
	session.commit()
	
