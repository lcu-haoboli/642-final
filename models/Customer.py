from . import Person
from sqlalchemy import  Column, Integer, String, ForeignKey,DateTime, DOUBLE,DECIMAL
class Customer(Person.Person):
	__tablename__="customer"
	# mapping

	custId = Column(Integer, ForeignKey("person.id"),primary_key = True)
	custAddress = Column(String(100))
	custBalance = Column(DECIMAL(precision=5, scale=2), nullable=True)
	maxOwning = Column(DECIMAL(precision=5, scale=2), nullable=True)

	def __init__(self,firstName: str, lastName: str, password: str, userName: str,userType: str, custId,custAddress,custBalance,maxOwing) -> None:
		super().__init__(firstName, lastName, password ,userName, userType) 
		self.custId = custId
		self.custAddress = custAddress
		self.custBalance = custBalance
		self.maxOwning = maxOwing

	def getCustAddress(self):
		return self.custAddress
	
class CorporateCustomer(Customer):
	# mapping
	__tablename__ = "corporateCustomer"
	corpCustId = Column(Integer, ForeignKey("customer.custId"), primary_key=True)
	discountRate = Column(DECIMAL(precision=5, scale=2))
	maxCredit = Column(DECIMAL(precision=5, scale=2))
	minBalance = Column(DECIMAL(precision=5, scale=2))

	def __init__(self, firstName, lastName, password, userName, custId, custAddress, custBalance, maxOwing, discountRate,maxCredit,minBalance):
		super().__init__(firstName, lastName, password, userName, custId, custAddress, custBalance, maxOwing)
		self.discountRate = discountRate
		self.maxCredit = maxCredit
		self.minBalance = minBalance



	