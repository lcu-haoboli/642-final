from abc import ABC


class Veggie(ABC):
	def __init__(self,vegName : str ) -> None:
		super().__init__()
		self._vegName = vegName
	
	@property
	def vegName(self):
		return self._vegName
	
	@vegName.setter
	def vegName(self, name):
		self._vegName = name
		

