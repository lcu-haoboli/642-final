from base import Base
from sqlalchemy import Column, String, Integer, DECIMAL ,FLOAT

class PremadeBox(Base):
	# mapping
	__tablename__ = "premade_box"
	preMadeboxId = Column(Integer, primary_key=True)
	boxSize = Column(String(50))
	numberOfBox = Column(Integer)

	def __init__(self, boxSize, numOfBoxes, boxContent) -> None:
		self.boxSize = boxSize
		self.numOfBoxes = numOfBoxes
		self.boxContent = boxContent
