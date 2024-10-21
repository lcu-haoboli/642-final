from abc import ABC


class Item(ABC):
	def __init__(self, itemName, itemPrice) -> None:
		super().__init__()
		self._itemName = itemName
		self._itemPrice = itemPrice

	

	

	
	
	