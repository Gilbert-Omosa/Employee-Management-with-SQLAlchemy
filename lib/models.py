from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    head = Column(String, nullable=False)

    employees = relationship('Employee', back_populates='department')

class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    job_group = Column(String, nullable=False)
    job_description = Column(Text, nullable=False)
    salary = Column(Integer, nullable=False)

    employees = relationship('Employee', back_populates='position')

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    date_hired = Column(DateTime(timezone=True), default=func.now())

    department_id = Column(Integer, ForeignKey('departments.id'))
    position_id = Column(Integer, ForeignKey('positions.id'))

    department = relationship('Department', back_populates='employees')
    position = relationship('Position', back_populates='employees')
