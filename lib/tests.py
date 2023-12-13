from main import *

# Test for sorting employees by name
def test_sort_employees_by_name():
    sorted_employees = sort_employees_by_name()
    print("\nSort employees by name:")
    for employee in sorted_employees:
        print(f"{employee.name}, Age: {employee.age}")

# Test for sorting employees by age
def test_sort_employees_by_age():
    sorted_employees = sort_employees_by_age()
    print("\nSort employees by age:")
    for employee in sorted_employees:
        print(f"{employee.name}, Age: {employee.age}")


test_sort_employees_by_name()
test_sort_employees_by_age()


