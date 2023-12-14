from config import session
from models import *
from datetime import datetime as DateTime
from config import *
from sqlalchemy import desc, func
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
#get all female employees above the age of 45 in each department
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

#years to retirement
def years_to_retirement(retirement_age):
    employees = session.query(Employee).all()

    years_to_retirement_dict = {}

    for employee in employees:
        years_left = retirement_age - employee.age

        if years_left > 0:
            years_to_retirement_dict[employee.name] = years_left
        else:
            print(f"Employee {employee.name} is already past retirement age.")

    return years_to_retirement_dict




#order employees by pay in descending order and get the sum of salary the organization pays
def salary_outlook():
    # Join Employee and Position tables and order by salary in descending order
    employees_ordered_by_salary = session.query(Employee).join(Position).order_by(desc(Position.salary)).all()

    # Calculate the sum of salaries
    total_salary = session.query(func.sum(Position.salary)).scalar()

    return employees_ordered_by_salary, total_salary

#calculate net salary of employee after deductions: 15% INCOME TAX , 5% HOUSING LEVY and 2% UNION FEES
def net_salary(employee_id):
    # Retrieve the employee and their position information
    employee = session.query(Employee).get(employee_id)
    position = employee.position

    if position is not None:
        # Calculate deductions
        income_tax_rate = 0.15
        housing_levy_rate = 0.05
        union_fees_rate = 0.02

        gross_salary = position.salary
        income_tax = gross_salary * income_tax_rate
        housing_levy = gross_salary * housing_levy_rate
        union_fees = gross_salary * union_fees_rate
        # Calculate net salary after deductions
        net_salary = gross_salary - income_tax - housing_levy - union_fees
        # Return detailed information
        result = {
            "employee_name": employee.name,
            "gross_salary": gross_salary,
            "deductions": {
                "income_tax": income_tax,
                "housing_levy": housing_levy,
                "union_fees": union_fees,
            },
            "net_salary": net_salary,
        }
        return result
    else:
        return None  # Handle the case where the employee has no associated position

#List employees by age range
def list_employees_by_age_range(min_age, max_age):
    employees_in_range = session.query(Employee).filter(Employee.age.between(min_age, max_age)).all()
    return employees_in_range

#find employee by email
def find_employees_by_email(email):
    return session.query(Employee).filter(Employee.email.ilike(f"%{email}%")).all()

# CRUD functions for the Department model
def create_department(name, description, head):
    department = Department(name=name, description=description, head=head)
    session.add(department)
    session.commit()
    return department

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
def create_position(title, job_group, job_description, salary):
    position = Position(title=title, job_group=job_group, job_description=job_description, salary=salary)
    session.add(position)
    session.commit()
    return position

def read_position(position_id):
    return session.query(Position).get(position_id)

def update_position(position_id, new_title, new_job_group, new_job_description, new_salary):
    position = session.query(Position).get(position_id)

    if new_title is not None and new_title != position.title:
        existing_position = session.query(Position).filter_by(title=new_title).first()
        if existing_position:
            print(f"Error: Position with title '{new_title}' already exists.")
            return None
        
    if new_title is not None:
        position.title = new_title
    if new_job_group is not None:
        position.job_group = new_job_group
    if new_job_description is not None:
        position.job_description = new_job_description
    if new_salary is not None:
        position.salary = new_salary

    session.commit()
    return position

def delete_position(position_id):
    position = session.query(Position).get(position_id)
    associated_employees = session.query(Employee).filter_by(position_id=position_id).all()
    for employee in associated_employees:
        session.delete(employee)
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
