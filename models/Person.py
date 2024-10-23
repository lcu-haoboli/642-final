from base import Base
from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT

class Person(Base):
	__tablename__ = "person"
	# mapping
	id =Column(Integer, primary_key=True)
	firstName = Column(String(50))
	lastName = Column(String(50))
	password = Column(String(50))
	userName = Column(String(50))



	# initor
	def __init__(self, firstName: str, lastName: str, password: str, userName: str) :
		self.firstName = firstName
		self.lastName = lastName
		self.password = password
		self.userName = userName





