from abc import ABC, abstractmethod


class Person(ABC):
	def __init__(
		self, firstName: str, lastName: str, password: str, userName: str
	) -> None:
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._password = password
		self._userName = userName

	@property
	def firstName(self):
		return self._firstName
	
	@firstName.setter
	def firstName(self, firstName:str):
		self._firstName = firstName
	
	@property
	def lastName(self):
		return self._lastName
	
	@property
	def password(self) -> str:
		return self._password

	@property
	def userName(self) -> str:
		return self._userName

	# Setters
	@firstName.setter
	def firstName(self, value: str):
		self._firstName = value

	@lastName.setter
	def lastName(self, value: str):
		self._lastName = value

	@password.setter
	def password(self, value: str):
		self._password = value

	@userName.setter
	def userName(self, value: str):
		self._userName = value

	@abstractmethod
	def getFullName(self):
		"""Return the fullName of this Person"""
		pass