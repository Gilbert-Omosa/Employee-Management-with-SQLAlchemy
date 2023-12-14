from main import *

# Eckra TESTS

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


department_id_legal = 1
department_id_Administration = 2
department_id_hr = 3

def test_count_employees_in_legal_department():
    count = count_employees_in_department(department_id_legal)
    print(f"\nEmployees in Legal Department: {count}")
    assert count >= 0  

# Test case 2: Count employees in the Administration department
def test_count_employees_in_administration_department():
    count = count_employees_in_department(department_id_Administration)
    print(f"Employees in Administration Department: {count}")
    assert count >= 0  

# Test case 3: Count employees in the Human Resources department
def test_count_employees_in_hr_department():
    count = count_employees_in_department(department_id_hr)
    print(f"Employees in Human Resources Department: {count}")
    assert count >= 0  

if __name__ == '__main__':
    
    test_count_employees_in_legal_department()
    test_count_employees_in_administration_department()
    test_count_employees_in_hr_department()
