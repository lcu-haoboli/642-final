from . import Person
from sqlalchemy import  Column, Integer, String, ForeignKey,DateTime,DECIMAL

class CorporateCustomer(Person.Person):
	# mapping
	__tablename__ = "corporateCustomer"
	corpCustId = Column(Integer, ForeignKey("person.id"),primary_key = True)
	discountRate = Column(DECIMAL(precision=5, scale=2))
	maxCredit = Column(DECIMAL(precision=5, scale=2))
	minBalance = Column(DECIMAL(precision=5, scale=2))

	def __init__(self,corpCustId, firstName, lastName, password, userName, userType,discountRate,maxCredit,minBalance):
		super().__init__(firstName, lastName, password, userName, userType)
		self.corpCustId = corpCustId
		self.discountRate = discountRate
		self.maxCredit = maxCredit
		self.minBalance = minBalance


	