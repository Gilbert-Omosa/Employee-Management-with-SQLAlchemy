from config import *
from sqlalchemy import desc, func
#--------CALEB FUNCTIONS-----------#
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
