
class OrderLine:
	def __init__(self, item, itemNumber) -> None:
		self._item = item
		self._itemNumber = itemNumber
	
	@property
	def item(self):
		return self._item
	
	@item.setter
	def item(self,value):
		self._item = value

	@property
	def itemNumber(self):
		return self._itemNumber
	
	@itemNumber.setter
	def itemNumber(self,value):
		self._item = value
