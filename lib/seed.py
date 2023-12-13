import random
from config import *

fake = Faker()

# Seed the database with some fake data
print("================ SEEDING STARTED ===============")

def seed_data():
    for _ in range(5):
        department_names = ["Administration", "Human Resources", "Finance", "Legal", "IT"]
        department_name = fake.random_element(elements=department_names)
        
        # Check if the department name already exists
        existing_department = session.query(Department).filter_by(name=department_name).first()
        if existing_department is None:
            department = Department(name=department_name, description=fake.paragraph(), head=fake.name())
            session.add(department)

    for _ in range(10):
        position = Position(title=fake.job(), job_group=fake.random_uppercase_letter(), job_description=fake.paragraph(), salary=random.randint(20000, 200000))
        session.add(position)
    
    for _ in range(15):
        employee = Employee(
            name=fake.name(),
            age=random.randint(18, 60),
            gender=fake.random_element(elements=("Male", "Female")),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
            date_hired=fake.date_this_decade(),
            position_id=random.randint(1, 10),
            department_id=random.randint(1, 5)
        )
        session.add(employee)

    session.commit()

seed_data()
session.close()
print("================ SEEDING COMPLETED ===============")