from config import Session
from models import Employee, Department, Position
from main import *

# Function to print a separator line for better readability
def print_separator():
    print("\n" + "=" * 40 + "\n")

# Function to check if an entity with a given ID exists
def entity_exists(model, entity_id):
    return session.query(model).filter_by(id=entity_id).first() is not None

# Test CRUD functions for Employee
# print_separator()
# print("Testing CRUD functions for Employees" + "\n")

# print("Creating an employee" + "\n")
# created_employee = create_employee(
#     name="Nerfertari Cobra",
#     age=54,
#     gender="Male",
#     email="0JpjE@example.com",
#     phone="123-456-7890",
#     address="123 Main Street",
#     date_hired="2022-01-01",
#     department_id=2,
#     position_id=3,
# )
# print("Employee",f" Name: {created_employee.name} Age: {created_employee.age} Created Successfully" + "\n")

# print("Fetching an employee using id" + "\n")
# if entity_exists(Employee, 8):
#     read_employee_result = read_employee(employee_id=8)
#     print("Fetched Employee Details are:", f" Name: {read_employee_result.name} Age: {read_employee_result.age}" + "\n")
# else:
#     print("Employee does not exist" + "\n")

# print("Updating an employee using id and new data" + "\n")
# update_data = {"name": "Dory Swimmer", "phone": "123-456-7890", "address": "42 Wallaby Way Sydney"}
# if entity_exists(Employee, 58):
#     updated_employee = update_employee(employee_id=58, new_data=update_data)
#     print("Updated Employee Details:", f" Name: {updated_employee.name} phone: {updated_employee.phone} address: {updated_employee.address}" + "\n")
# else:
#     print("Employee does not exist" + "\n")

# print("Deleting an employee using id" + "\n")
# if entity_exists(Employee, 21):
#     deleted_employee = delete_employee(employee_id = 21)
#     print("Deleted Employee Successfully" + "\n")
# else:
#     print("Employee does not exist" + "\n")

# # Test CRUD functions for Department
print_separator()
print("Testing CRUD functions for Department" + "\n")

# print("Creating a department" + "\n")
# created_department = create_department(name="IT", description="Information Technology department", head="Levi Ackerman")
# print(f"{created_department.name} Department Created Successfully" + "\n")

print("Fetching a department using id" + "\n")
if entity_exists(Department, 8):
    read_department_result = read_department(department_id = 8)
    print("Fetched Department Details:", f"Name: {read_department_result.name} Description: {read_department_result.description} Head: {read_department_result.head}" + "\n")
else:
    print("Department does not exist" + "\n")

# # Update a department
# updated_department = update_department(created_department.id, new_name="Marketing")
# if entity_exists(Department, created_department.id):
#     print("Updated Department:", updated_department)
# else:
#     print("Department does not exist")

# # Delete a department
# if entity_exists(Department, created_department.id):
#     deleted_department = delete_department(created_department.id)
#     print("Deleted Department:", deleted_department)
# else:
#     print("Department does not exist")

# # Test CRUD functions for Position
# print_separator()
# print("Testing CRUD functions for Position")

# # Create a position
# created_position = create_position(title="Software Engineer", salary=80000)
# print("Created Position:", created_position)

# # Read a position
# if entity_exists(Position, created_position.id):
#     read_position_result = read_position(created_position.id)
#     print("Read Position:", read_position_result)
# else:
#     print("Position does not exist")

# # Update a position
# updated_position = update_position(created_position.id, new_title="Senior Software Engineer", new_salary=90000)
# if entity_exists(Position, created_position.id):
#     print("Updated Position:", updated_position)
# else:
#     print("Position does not exist")

# # Delete a position
# if entity_exists(Position, created_position.id):
#     deleted_position = delete_position(created_position.id)
#     print("Deleted Position:", deleted_position)
# else:
#     print("Position does not exist")

# # Test fetching employees by position
# print_separator()
# print("Testing fetching employees by position")

# # Fetch employees by position
# employees_by_position_result = fetch_employees_by_position(position_id=1)
# print("Employees by Position:", employees_by_position_result)

# # Test fetching employees by department and position
# print_separator()
# print("Testing fetching employees by department and position")

# # Fetch employees by department and position
# employees_by_department_and_position_result = fetch_employees_by_department_and_position(department_id=1, position_id=1)
# print("Employees by Department and Position:", employees_by_department_and_position_result)

# # Closing session explicitly for clarity (assuming you open a new session for each test)
# Session().close()
