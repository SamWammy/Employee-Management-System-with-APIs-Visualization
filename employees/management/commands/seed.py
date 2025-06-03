from django.core.management.base import BaseCommand
from faker import Faker 
from employees.models import employees
from employees.models import department
from performance.models import performance
from attendence.models import attendence
import random

class Command(BaseCommand):
    help = 'Seed Database with faker'

    def handle( self, *args,**kwargs):
        fake = Faker()

        temp= ['HR',
               "Engineering",
                        "Marketing",
                        "Finance",
                        "Sales",
                        "Administration",
                        "IT"]
        
            #employee seeding for 30 employees
        departments=[]
        for i in range(len(temp)):
            depo= department.objects.create(
                department = temp[i]
            )
            departments.append(depo)

        for _ in range(30):
            employees.objects.create(
                name= fake.name(),
                email = fake.email(),
                phoneNumber = fake.phone_number(),
                address = fake.address(),
                dateOfJoining= fake.date_between(start_date="-5y", end_date="today"),
                department = random.choice(departments)
            )
        employee_ids= list(employees.objects.all())


        # this is for performance seeding in the data base
        for _ in range(30):
            performance.objects.create(
                employee = random.choice(employee_ids),
                rating = random.randint(1,5),
                reviewDate = fake.date_between(start_date="-5y",end_date="today"),
            )
        

        #this is the database seeding for attendence 
        attendence_choices=["present","late","absent"]
        for _ in range(30):
            attendence.objects.create(
                employeeName = random.choice(employee_ids),
                date= fake.date_between(start_date="-5y",end_date="today"),
                status = random.choice(attendence_choices),
            )


        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))

    