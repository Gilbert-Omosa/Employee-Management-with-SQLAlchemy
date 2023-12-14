from main import *

print(">>>>>>>>>>>> CALEB FUNCTIONS <<<<<<<<<<<")
print("***** get all female employees above the age of 45 in each department *****")
result = females_above_age_45()
for department, employees in result.items():
    print(f"Department: {department}")
    for employee in employees:
        print(f"  Employee: {employee.name}, Age: {employee.age}")
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

print(">>>>>>>>>>>> <<<<< >>>>> <<<<<<<<<<<")




