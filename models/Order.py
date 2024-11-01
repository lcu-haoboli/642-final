from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT,ForeignKey,DATETIME
from base import Base

class Order(Base):
	# mapping
	__tablename__ = "order"
	orderId = Column(Integer, primary_key=True)
	orderCustomer = Column(Integer)
	orderDate = Column(DATETIME)
	# paid, shipping, delivered, close
	orderStatus = Column(String(50))
	oderType = Column(String(50), nullable=True)


	def __init__(self, orderCustomer, orderDate,orderStatus,oderType) -> None:
		self.orderCustomer = orderCustomer
		self.orderDate = orderDate
		self.orderStatus = orderStatus
		self.oderType = oderType
	
