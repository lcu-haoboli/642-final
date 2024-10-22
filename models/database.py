from sqlalchemy import create_engine
from . import Veggie
from base import Base, session

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/veggie_shop",echo=True)


def init_db():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)

	veggie = Veggie.Veggie("bok choy")
	print(veggie.vegName)
	session.add(veggie)
	session.commit()
	