from sqlalchemy import create_engine
from . import Veggie
from . import Person
from .import Staff
from base import Base, session
from datetime import date

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/veggie_shop",echo=True)


def init_db():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)

	veggie = Veggie.Veggie("bok choy")
	# person = Person.Person()
	today =  date.today()
	staff = Staff.Staff("kevin", "li", "1234", "kevinli",1, today, "hello-dep", "abcd",None, None)
	session.add(veggie)
	# session.add(person)
	session.add(staff)
	session.commit()
	