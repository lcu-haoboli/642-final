from base import Base
from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT,ForeignKey

class OrderLine(Base):
	# mapping
	__tablename__ = "order_line"
	orderLineId = Column(Integer, primary_key=True)
	orderId = Column(Integer,ForeignKey("order.orderId"))
	veggieId = Column(Integer, nullable=True)
	premadeBoxId = Column(Integer, nullable=True)
	orderQuantity = Column(Integer)

	def __init__(self, orderId, veggieId, premadeBoxId,orderQuantity) -> None:
		self.orderId = orderId
		self.veggieId = veggieId
		self.premadeBoxId = premadeBoxId
		self.orderQuantity = orderQuantity
	