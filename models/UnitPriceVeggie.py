from Veggie import Veggie

def UnitPriceVeggie(Veggie):
	def __init__(self,pricePerUnit,quantity, *args):
		super().__init__(*args)
		self._pricePerUnit = pricePerUnit
		self._quantity = quantity

		@property
		def pricePerUnit(self):
			return self._pricePerUnit
		
		@pricePerUnit.setter
		def pricePerUnit(self,value):
			self._pricePerUnit = value
		
		@property
		def quantity(self):
			return self._quantity

		@quantity.setter
		def quantity(self,value):
			self._quantity = value
		
def totalPrice(self):
	return self._pricePerUnit * self._quantity
	
	
		

