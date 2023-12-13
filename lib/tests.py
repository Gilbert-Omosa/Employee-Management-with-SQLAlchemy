from main import *

print(">>>>>>>>>>>> EVAN FUNCTIONS <<<<<<<<<<<")
print("***** transfering an employee from one department to another *****")

# Replace with actual data or create a new employee for testing
employee_id_to_transfer = 1
new_department_id = 2

# Fetch the employee before transfer
original_employee = session.query(Employee).get(employee_id_to_transfer)
original_department_id = original_employee.department_id

# Perform the transfer
transferred_employee = transfer_employee(original_employee, new_department_id)

# Fetch the employee after transfer
updated_employee = session.query(Employee).get(employee_id_to_transfer)

# Print the results
print(f"Transferred Employee: {transferred_employee.name}")
print(f"Original Department: {original_department_id}")
print(f"Updated Department: {transferred_employee.department_id}")

print(">>>>>>>>>>>> <<<<< END OF TESTS >>>>> <<<<<<<<<<<")