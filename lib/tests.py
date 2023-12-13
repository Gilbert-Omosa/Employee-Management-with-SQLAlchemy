from main import *

print(">>>>>>>>>>>> CALEB FUNCTIONS <<<<<<<<<<<")
print("***** get all female employees above the age of 45 in each department *****")
result = females_above_age_45()
for department, employees in result.items():
    print(f"Department: {department}")
    for employee in employees:
        print(f"  Employee: {employee.name}, Age: {employee.age}")

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
