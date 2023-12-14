from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Employee, Department, Position
from random import randint

# Set Up SQLite database engine
engine = create_engine("sqlite:///database.sqlite")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()