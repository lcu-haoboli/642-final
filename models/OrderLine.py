from base import Base
from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT

class OrderLine:
	# mapping
	__tablename__ = "order_line"
	orderLineId = Column(Integer, primary_key=True)
	orderId = Column(Integer,ForeignKey = "order.orderId")
	veggieId = Column(Integer, nullable=True)
	premadeBoxId = Column(Integer, nullable=True)

	def __init__(self, orderId, veggieId, premadeBoxId) -> None:
		self.orderId = orderId
		self.veggieId = veggieId
		self.premadeBoxId = premadeBoxId
	