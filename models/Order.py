
class Order:
	def __init__(self, orderCustomer, orderDate,orderNumber,orderStatus) -> None:
		self._orderCustomer = orderCustomer
		self._orderDate = orderDate
		self.orderNumber = orderNumber
		self._orderStatus = orderStatus
	

	@property
	def orderCustomer(self):
		return self._orderCustomer
	
	@orderCustomer.setter
	def orderCustomer(self, customer):
		self._orderCustomer = customer
	
	@property
	def orderDate(self):
		return self._orderDate

	@orderDate.setter
	def orderDate(self, orderDate):
		self.orderDate = orderDate
	
	@property
	def orderNumber(self):
		return self._orderNumber
	
	@orderNumber.setter
	def orderNumber(self, number):
		self._orderNUmber = number
	
	@property
	def orderStatus(self):
		return self._orderStatus
	
	@orderStatus.setter
	def orderStatus(self,value):
		self._orderStatus = value



		