from Person import Person
class Customer(Person):
	def __init__(self,custAddress,custBalance,custID,maxOwing, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self._custAddress = custAddress
		self._custID = custID
		self._cusBalance = custBalance
		self._maxOwning = maxOwing
	
	@property
	def custAddress(self):
		return self._custAddress
	
	@custAddress.setter
	def custAddress(self, value):
		self._custAddress = value
	
	@property
	def custBalance(self):
		return self._cusBalance

	@custBalance.setter
	def custBalance(self, value):
		self._cusBalance = value
	
	@property
	def maxOwning(self):
		return self._maxOwning
	
	@maxOwning.setter
	def maxOwning(self,value):
		self._maxOwning = value

	# some method might needed 