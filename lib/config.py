from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Employee, Department, Position

# Set Up SQLite database engine
engine = create_engine("sqlite:////Users/ms/Desktop/Development/Employee-Management-with-SQLAlchemy/database.sqlite")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()