from sqlalchemy import  Column, Integer, String, ForeignKey,DATETIME,DECIMAL
from base import Base
class Payment(Base):
	# mapping
	__tablename__ = "payment"
	paymentId = Column(Integer,primary_key=True)
	custId = Column(Integer, ForeignKey("person.id"))
	orderId = Column(Integer, ForeignKey("order.orderId"))
	paymentAmount = Column(DECIMAL(precision=5, scale=2))
	paymentDate = Column(DATETIME)
	paymentType = Column(String(50))
	cardExpireDate = Column(DATETIME, nullable=True)
	bankName = Column(String(50), nullable=True)
	debitCardNumber = Column(String(50),nullable=True)

	__mapper_args__ = {
        'polymorphic_identity': 'payment',
        'polymorphic_on': paymentType
    }

	def __init__(self, custId, orderId, paymentAmount, paymentDate,):
		self.custId = custId
		self.orderId = orderId
		self.paymentAmount = paymentAmount
		self.paymentDate = paymentDate

class CreditCardPayment(Payment):
	__mapper_args__ = {
		'polymorphic_identity': 'creditCardPayment',
	}

	def __init__(self,custId,orderId, paymentAmount, paymentDate,cardExpireDate):
		super().__init__(custId,orderId, paymentAmount, paymentDate)
		self.cardExpireDate = cardExpireDate
		

class DebitCardPayment(Payment):
	__mapper_args__ = {
		'polymorphic_identity': 'debitCardPayment',
	}

	def __init__(self,custId,orderId, paymentAmount, paymentDate, bankName,debitCardNumber):
		super().__init__(custId,orderId, paymentAmount, paymentDate)
		self.bankName = bankName
		self.debitCardNumber = debitCardNumber

