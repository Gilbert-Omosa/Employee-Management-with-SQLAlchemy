from config import *
from models import *
from datetime import datetime as DateTime

# CRUD functions for the Employee model
def create_employee(name, age, gender, email, phone, address, date_hired, department_id, position_id):

    # Convert date_hired string to datetime object
    date_hired = DateTime.strptime(date_hired, '%Y-%m-%d')

    employee = Employee(
        name=name,
        age=age,
        gender=gender,
        email=email,
        phone=phone,
        address=address,
        date_hired=date_hired,
        department_id=department_id,
        position_id=position_id
    )
    session.add(employee)
    session.commit()
    return employee

def read_employee(employee_id):
    return session.query(Employee).get(employee_id)

def update_employee(employee_id, new_data):
    employee = session.query(Employee).get(employee_id)
    for key, value in new_data.items():
        setattr(employee, key, value)
    session.commit()
    return employee

def delete_employee(employee_id):
    employee = session.query(Employee).get(employee_id)
    session.delete(employee)
    session.commit()
    return employee

# CRUD functions for the Department model
def create_department(name, description, head):
    department = Department(name=name, description=description, head=head)
    session.add(department)
    session.commit()
    return department

def read_department(department_id):
    return session.query(Department).get(department_id)

def update_department(department_id, new_name, new_description, new_head):
    department = session.query(Department).get(department_id)

    # Check if the new name is already in use
    if new_name is not None and new_name != department.name:
        existing_department = session.query(Department).filter_by(name=new_name).first()
        if existing_department:
            print(f"Error: Department with name '{new_name}' already exists.")
            return None

    # Update the department attributes
    if new_name is not None:
        department.name = new_name
    if new_description is not None:
        department.description = new_description
    if new_head is not None:
        department.head = new_head
        
    session.commit()
    return department

def delete_department(department_id):
    department = session.query(Department).get(department_id)
    associated_employees = session.query(Employee).filter_by(department_id=department_id).all()
    for employee in associated_employees:
        session.delete(employee)
    session.delete(department)
    session.commit()
    return department

# CRUD functions for the Position model
def create_position(title, salary):
    position = Position(title=title, salary=salary)
    session.add(position)
    session.commit()
    return position

def read_position(position_id):
    return session.query(Position).get(position_id)

def update_position(position_id, new_title, new_salary):
    position = session.query(Position).get(position_id)
    position.title = new_title
    position.salary = new_salary
    session.commit()
    return position

def delete_position(position_id):
    position = session.query(Position).get(position_id)
    session.delete(position)
    session.commit()
    return position

# Fetching employees by position
def fetch_employees_by_position(position_id):
    employees_by_position = session.query(Employee).filter(Employee.position_id == position_id).all()
    return employees_by_position

# Fetching employees by department and position
def fetch_employees_by_department_and_position(department_id, position_id):
    employees_by_department_and_position = session.query(Employee).filter(Employee.department_id == department_id, Employee.position_id == position_id).all()
    return employees_by_department_and_position

session.close()