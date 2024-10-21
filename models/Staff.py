from Person import Person
from datetime import date

class Staff(Person):
	def __init__(self, staffID: int, dateJoined: date, deptName:str,listOfOrder,premadeBoxes,veggie, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._staffID = staffID
		self._dateJoined = dateJoined
		self._deptName = deptName
		self._listOfOrder = listOfOrder
		self._premadeBoxes = premadeBoxes
		self._veggie = veggie

	@property
	def staffID(self) -> int:
		return self._staffID

	@staffID.setter
	def staffID(self, value: int):
		self._staffID = value

	@property
	def dateJoined(self) -> str:
		return self._dateJoined

	@dateJoined.setter
	def role(self, dateJoined: date):
		self._dateJoined = dateJoined

	@property
	def listOfOrder(self) -> list:
		return self._listOfOrder

	@listOfOrder.setter
	def listOfOrder(self, listOfOrder):
		self._listOfOrder = listOfOrder
		
	@property
	def deptName(self):
		return self._deptName

	@deptName.setter
	def deptName(self,value):
		self._deptName = value

	@property
	def premadeBoxes(self):
		return self._premadeBoxes
	
	@premadeBoxes.setter
	def premadeBoxes(self,premadeBoxes):
		self._premadeBoxes = premadeBoxes

	
	@property
	def veggie(self):
		return self._veggie
	
	@veggie.setter
	def veggie(self,value):
		self._veggie = value
		

	def getFullName(self):
		return f"{self.firstName} {self.lastName}"