from sqlalchemy import  Column, Integer, String, ForeignKey,DATETIME, DOUBLE,DECIMAL
from base import Base
class Payment(Base):
	# mapping
	paymentId = Column(Integer,primary_key=True)
	custId = Column(Integer, ForeignKey=("customer.custId"))
	paymentAmount = Column(DECIMAL(precision=5, scale=2))
	paymentDate = Column(DATETIME)

	def __init__(self, custId, paymentAmount, paymentDate):
		self.custId = custId,
		self.paymentAmount = paymentAmount
		self.paymentDate = paymentDate

