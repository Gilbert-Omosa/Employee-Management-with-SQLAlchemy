<<<<<<< HEAD

=======
from config import *
from models import Employee, Department, Position
from main import *

# Function to print a separator line for better readability
def print_separator():
    print("\n" + "=" * 40 + "\n")

# Function to check if an entity with a given ID exists
def entity_exists(model, entity_id):
    return session.query(model).filter_by(id=entity_id).first() is not None

# Test CRUD functions for Employee
print_separator()
print("Testing CRUD functions for Employees" + "\n")

print("Creating an employee" + "\n")
created_employee = create_employee(
    name="Nerfertari Cobra",
    age=54,
    gender="Male",
    email="0JpjE@example.com",
    phone="123-456-7890",
    address="123 Main Street",
    date_hired="2022-01-01",
    department_id=2,
    position_id=3,
)
print("Employee",f" Name: {created_employee.name} Age: {created_employee.age} Created Successfully" + "\n")

print("Fetching an employee using id" + "\n")
if entity_exists(Employee, 8):
    read_employee_result = read_employee(employee_id=8)
    print("Fetched Employee Details are:", f" Name: {read_employee_result.name} Age: {read_employee_result.age}" + "\n")
else:
    print("Employee does not exist" + "\n")

print("Updating an employee using id and new data" + "\n")
update_data = {"name": "Dory Swimmer", "phone": "123-456-7890", "address": "42 Wallaby Way Sydney"}
if entity_exists(Employee, 58):
    updated_employee = update_employee(employee_id=58, new_data=update_data)
    print("Updated Employee Details:", f" Name: {updated_employee.name} phone: {updated_employee.phone} address: {updated_employee.address}" + "\n")
else:
    print("Employee does not exist" + "\n")

print("Deleting an employee using id" + "\n")
if entity_exists(Employee, 21):
    deleted_employee = delete_employee(employee_id = 21)
    print("Deleted Employee Successfully" + "\n")
else:
    print("Employee does not exist" + "\n")

# # Test CRUD functions for Department
print_separator()
print("Testing CRUD functions for Department" + "\n")

print("Creating a department" + "\n")
created_department = create_department(name="IT", description="Information Technology department", head="Levi Ackerman")
print(f"{created_department.name} Department Created Successfully" + "\n")

print("Fetching a department using id" + "\n")
if entity_exists(Department, 8):
    read_department_result = read_department(department_id = 8)
    print("Fetched Department Details:", f"Name: {read_department_result.name} Description: {read_department_result.description} Head: {read_department_result.head}" + "\n")
else:
    print("Department does not exist" + "\n")

print("Update a department using id and new data" + "\n")
updated_department = update_department(department_id = 4, new_name = "Advertising", new_description = "Marketing department", new_head = "Oswald Cobblepot")
if entity_exists(Department, 4):
    print("Updated Department Details:", f"Name: {updated_department.name} Description: {updated_department.description} Head: {updated_department.head}" + "\n")
else:
    print("Department does not exist" + "\n")

print("Deleting a department" + "\n")
if entity_exists(Department, 5):
    deleted_department = delete_department(department_id = 5)
    print("Deleted Department Successfully" + "\n")
else:
    print("Department does not exist" + "\n")

# # Test CRUD functions for Position
print_separator()
print("Testing CRUD functions for Position" + "\n")

print("Creating a position" + "\n")
created_position = create_position(title="Front Desk Receptionist", job_group="Receptionists", job_description="Receive guests and perform administrative duties", salary=50000)
print(f"{created_position.title} Position Created Successfully" + "\n")

print("Fetching a position using id" + "\n")
if entity_exists(Position, 11):
    read_position_result = read_position(position_id=11)
    print("Fetched Position Details:", f"Title: {read_position_result.title} Job Group: {read_position_result.job_group} Job Description: {read_position_result.job_description} Salary: {read_position_result.salary}" + "\n")
else:
    print("Position does not exist" + "\n")

print("Update a position using id and new data" + "\n")
updated_position = update_position(position_id=2, new_title="Gate Keeper", new_job_group="Security", new_job_description="Control access to the building", new_salary=30000)
if entity_exists(Position, 2):
    print("Updated Position Details:", f"Title: {updated_position.title} Job Group: {updated_position.job_group} Job Description: {updated_position.job_description} Salary: {updated_position.salary}" + "\n")
else:
    print("Position does not exist" + "\n")

print("Deleting a position" + "\n")
if entity_exists(Position, 3):
    deleted_position = delete_position(position_id=3)
    print("Deleted Position Successfully" + "\n")
else:
    print("Position does not exist" + "\n")

# # Test fetching employees by position
print_separator()
print("Testing fetching employees by position" + "\n")

print("Fetch employees by position" + "\n")
employees_by_position_result = fetch_employees_by_position(position_id=7)
for employee in employees_by_position_result:
    print("Employee by Position:")
    print("Name:", employee.name)
    print("Age:", employee.age)
    print("Phone:", employee.phone)
    print("Address:", employee.address)
    print("\n")

# Test fetching employees by department and position
print_separator()
print("Testing fetching employees by department and position" + "\n")

print("Fetching employees by department and position" + "\n")

employees_by_department_and_position_result = fetch_employees_by_department_and_position(department_id=3, position_id=8)

for employee in employees_by_department_and_position_result:
    print("Employee by Department and Position:")
    print("Name:", employee.name)
    print("Age:", employee.age)
    print("Phone:", employee.phone)
    print("Address:", employee.address)
    print("\n")
print(">>>>>>>>>>>> CALEB FUNCTIONS <<<<<<<<<<<")
print("***** Calculates years to retirement *****")
retirement_age = 65  # Replace with the actual retirement age
retirement_info = years_to_retirement(retirement_age)
print(f"Years to Retirement for Employees:")
for employee_name, years_left in retirement_info.items():
    print(f"{employee_name}: {years_left} years left to retirement")

print("***** Employees ordered by salary in descending order and get Sum: *****")
ordered_employees, total_salary = salary_outlook()
for employee in ordered_employees:
    print(f"  Employee: {employee.name}, Salary: {employee.position.salary}")

print(f"\nTotal organization salary: KSH {total_salary}")
print("*****Calculate net salary of employee after deductions: 15% INCOME TAX , 5% HOUSING LEVY and 2% UNION FEES*****")
employee_id_to_calculate = 1  # Replace with the actual employee_id
result = net_salary(employee_id_to_calculate)
if result:
    print(f"Detailed Salary Calculation for Employee ID {employee_id_to_calculate} ({result['employee_name']}):")
    print(f"Gross Salary: {result['gross_salary']}")
    print(f"Deductions:")
    print(f"  Income Tax: {result['deductions']['income_tax']}")
    print(f"  Housing Levy: {result['deductions']['housing_levy']}")
    print(f"  Union Fees: {result['deductions']['union_fees']}")
    print(f"Net Salary: {result['net_salary']}")
else:
    print(f"No position information found for Employee ID {employee_id_to_calculate}.")

print("*****Find employee by age range*****")
min_age=18
max_age=40
result = list_employees_by_age_range(min_age, max_age)
for employee in result:
    print(f"Employee Name: {employee.name} - Age: {employee.age}")
print("*****Find employee by email*****")
email= "vmiller@example.org"
result = find_employees_by_email(email)
for employee in result:
    print(f"Employee Name: {employee.name} - Email: {employee.email}")
    
print("***** get all female employees above the age of 45 in each department *****")
result = females_above_age_45()
for department, employees in result.items():
    print(f"Department: {department}")
    for employee in employees:
        print(f"  Employee: {employee.name}, Age: {employee.age}")

print(">>>>>>>>>>>> <<<<< >>>>> <<<<<<<<<<<")
Session().close()
>>>>>>> origin/Gilbert
