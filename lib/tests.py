from main import *
from faker import Faker


faker = Faker()

print(">>>>>>>>>>>> EVAN FUNCTIONS <<<<<<<<<<<")
print("***** TESTING: transferring an employee from one department to another *****")

# Replace with actual data or create a new employee for testing
employee_id_to_transfer = 11
new_department_id = 1

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


print("***** TESTING: getting department with the highest salary expense *****")

result = get_department_with_highest_salary_expense()

if result:
    department_name, total_salary = result
    print(f"Department with Highest Salary Expense: {department_name}")
    print(f"Total Salary Expense: KSH {total_salary}")
else:
    print("No departments found.")


print("***** TESTING: fetching employees from each department *****")

employees_by_department = list_employees_by_department()

if employees_by_department:
    print("Employees grouped by department:")
    for department_id, count in employees_by_department:
        department_name = session.query(Department.name).filter_by(id=department_id).scalar()
        print(f"  Department: {department_name}, Count: {count}")
else:
    print("No employee data available.")

