from . import Person
from datetime import date
from sqlalchemy import  Column, Integer, String, ForeignKey,DateTime
from base import Base

class Staff(Person.Person, Base):
	__tablename__ = "staff"
	# mapping
	staffId = Column(Integer, ForeignKey("person.id"),primary_key = True)
	dateJoined = Column(DateTime)
	deptName = Column(String(50))
	listOfOrder = Column(String(100), nullable=True)
	premadeBoxes = Column(String(50),nullable=True)
	veggie = Column(String(50), nullable=True)


	def __init__(self,firstName: str, lastName: str, password: str, userName: str,userType:str, staffId: int, dateJoined: date, deptName:str,listOfOrder,premadeBoxes,veggie):
		super().__init__(firstName, lastName, password ,userName,userType) 
		self.staffId = staffId
		self.dateJoined = dateJoined
		self.deptName = deptName
		self.listOfOrder = listOfOrder
		self.premadeBoxes = premadeBoxes
		self.veggie = veggie
