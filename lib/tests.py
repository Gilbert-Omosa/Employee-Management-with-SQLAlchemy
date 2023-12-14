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

#Count employees in the Administration department

def test_count_employees_in_legal_department():
    count = count_employees_in_department(department_id_legal)
    print(f"\nEmployees in Legal Department: {count}")
    assert count >= 0  

#  Count employees in the Administration department
def test_count_employees_in_administration_department():
    count = count_employees_in_department(department_id_Administration)
    print(f"Employees in Administration Department: {count}")
    assert count >= 0  

#  Count employees in the Human Resources department
def test_count_employees_in_hr_department():
    count = count_employees_in_department(department_id_hr)
    print(f"Employees in Human Resources Department: {count}")
    assert count >= 0  

if __name__ == '__main__':
    
    test_count_employees_in_legal_department()
    test_count_employees_in_administration_department()
    test_count_employees_in_hr_department()
    
#  search_positions_by_job_group_and_salary_range function for all job groups
def test_search_positions_for_all_groups():
    # Define a list of job groups to test
    job_groups = ['J', 'K', 'C', 'E', 'Y', 'X', 'Z', 'M', 'P']
    min_salary = 50000
    max_salary = 100000
    
    for job_group in job_groups:
        positions = search_positions_by_job_group_and_salary_range(job_group, min_salary, max_salary)
        
        print("\nPositions in Job Group {} with Salary Range {} - {}:".format(job_group, min_salary, max_salary))
        for position in positions:
            print("ID: {}, Title: {}, Salary: {}".format(position.id, position.title, position.salary))


test_search_positions_for_all_groups()

    

