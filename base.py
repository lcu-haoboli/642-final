from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker




engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/veggie_shop",echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


