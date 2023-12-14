from config import *
from sqlalchemy import func

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

# <----Evan's Functions ------>


# Transfering an employee to another department
def transfer_employee(employee, new_department_id):
    employee.department_id = new_department_id
    session.commit() 
    return employee

# Shows the department with the highest money spent
def get_department_with_highest_salary_expense():
    result = (
        session.query(Department.name, func.sum(Position.salary).label('total_salary'))
        .join(Employee, Employee.department_id == Department.id)
        .join(Position, Position.id == Employee.position_id)
        .group_by(Department.id)
        .order_by(func.sum(Position.salary).desc())
        .first()
    )
    return result

#Creates a list of employees in each department

def list_employees_by_department():
    employees_by_department = (
        session.query(Employee.department_id, func.count(Employee.id))
        .group_by(Employee.department_id)
        .all()
    )
    return employees_by_department
 

session.close()