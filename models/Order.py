from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT,ForeignKey,DATETIME
from base import Base

class Order(Base):
	# mapping
	__tablename__ = "order"
	orderId = Column(Integer, primary_key=True)
	orderCustomer = Column(Integer, ForeignKey=("customer.custId"))
	orderDate = Column(DATETIME)
	orderStatus = Column(String(50))

	def __init__(self, orderCustomer, orderDate,orderNumber,orderStatus) -> None:
		self.orderCustomer = orderCustomer
		self.orderDate = orderDate
		self.orderNumber = orderNumber
		self.orderStatus = orderStatus
	
