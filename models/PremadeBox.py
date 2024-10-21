
class PremadeBox:
	def __init__(self, boxSize, numOfBoxes, boxContent) -> None:
		self._boxSize = boxSize
		self._numOfBoxes = numOfBoxes
		self._boxContent = boxContent

		@property
		def boxSize(self):
			return self._boxSize
		
		@boxSize.setter
		def boxSize(self, size):
			self._boxSize = size


		@property
		def numOfBoxes(self):
			return self._numOfBoxes
			
		@numOfBoxes
		def numOfBoxes(self, num):
			self._numOfBoxes = num

		@property
		def boxContent(self):
			return self._boxContent

		@boxContent.setter
		def boxContent(self, content):
			self._boxContent = content

	def boxPrice(self):
			return self.numOfBoxes * self.boxSize
		
			
		