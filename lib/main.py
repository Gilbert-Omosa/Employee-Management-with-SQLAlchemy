from config import *
from sqlalchemy import desc, func
from sqlalchemy.orm import joinedload
# CRUD functions for the Employee model
def create_employee(name, age, gender, email, phone, address, hire_date, department_id, position_id):
    employee = Employee(
        name=name,
        age=age,
        gender=gender,
        email=email,
        phone=phone,
        address=address,
        hire_date=hire_date,
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
def create_department(name):
    department = Department(name=name)
    session.add(department)
    session.commit()
    return department

def read_department(department_id):
    return session.query(Department).get(department_id)

def update_department(department_id, new_name):
    department = session.query(Department).get(department_id)
    department.name = new_name
    session.commit()
    return department

def delete_department(department_id):
    department = session.query(Department).get(department_id)
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

#--------CALEB FUNCTIONS-----------#
# get all female employees above the age of 45 in each department
def females_above_age_45():
    # query to select all female employees who are older than 45
    female_employees= session.query(Employee).filter(Employee.gender == "Female", Employee.age > 45).all()

    #Group employees by department
    employees_by_department={}
    for employee in female_employees:
        department= employee.department
        if department is not None:
            department_name = department.name
            department_name= employee.department.name
            if department_name not in  employees_by_department:
                employees_by_department[department_name]=[]
            employees_by_department[department_name].append(employee)
    return employees_by_department

#order employees by pay in descending order and get the sum of salary the organization pays
def salary_outlook():
    # Join Employee and Position tables and order by salary in descending order
    employees_ordered_by_salary = session.query(Employee).join(Position).order_by(desc(Position.salary)).all()

    # Calculate the sum of salaries
    total_salary = session.query(func.sum(Position.salary)).scalar()

    return employees_ordered_by_salary, total_salary



