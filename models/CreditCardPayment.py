from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT,ForeignKey,DATETIME
from base import Base

class CreditCardPayment(Base):
	# mapping 
	paymentId = Column(Integer, ForeignKey("payment.paymentId"), primary_key=True)
	cardExpireDate = Column(DATETIME)
	cardType = Column(String)

	def __init__(self,paymentId, cardExpireDate,cardType):
		self.paymentId = paymentId
		self.cardExpireDate = cardExpireDate
		self.cardType = cardType

