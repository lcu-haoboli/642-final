from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT,ForeignKey,DATETIME
from base import Base

class DebitCardPayment(Base):
	# mapping 
	paymentId = Column(Integer, ForeignKey("payment.paymentId"), primary_key=True)
	bankName = Column(String(50))
	debitCardNumber = Column(String(50))

	def __init__(self,paymentId, bankName,debitCardNumber):
		self.paymentId = paymentId
		self.bankName = bankName
		self.debitCardNumber = debitCardNumber

