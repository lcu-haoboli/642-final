from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT
from base import Base

class Veggie(Base):
	__tablename__ = "veggie"
	id = Column(Integer, primary_key=True)
	vegName = Column(String(100)) 
	pricePerUnit = Column(DECIMAL(2), nullable = True) # unit veggie
	quantity = Column(Integer, nullable = True) # unit veggie
	numOfPack = Column(Integer, nullable = True) # pack veggie
	pricePerPack = Column(DECIMAL(2), nullable = True) # pack veggie
	weight = Column(FLOAT) # weight veggie
	pricePerKiol = Column(DECIMAL(2), nullable = True) # weight veggie
	type = Column(String(50)) # discriminator


	__mapper_args__ = {
        'polymorphic_identity': 'veggie',
        'polymorphic_on': type
    }

	def __init__(self, vegName, pricePerUnit=None, quantity=None, numOfPack=None, pricePerPack=None, weight=None, pricePerKiol=None):
		self.vegName = vegName

	
class UnitPriceVeggie(Veggie):
	__mapper_args__ = {
		'polymorphic_identity': 'unitPriceVeggie',
	}

	def __init__(self, vegName, pricePerUnit, quantity):
		super().__init__(vegName)
		self.pricePerUnit = pricePerUnit
		self.quantity = quantity
	
	def __str__(self):
		return f"{self.vegName} {self.type} {self.pricePerUnit} {self.quantity}"
	
class WeightedVeggie(Veggie):
	__mapper_args__ = {
		'polymorphic_identity': 'weightedVeggie',
	}

	def __init__(self, vegName,  weight, pricePerKiol):
		super().__init__(vegName)
		self.weight = weight
		self.pricePerKiol = pricePerKiol

	def __str__	(self):
		return f"{self.vegName} {self.weight} {self.pricePerKiol}"




		


