import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','database_proj.settings')
import django
django.setup()



from firstapp.models import *
from faker import  Faker
from random import *
faker = Faker()

def populate(n):
    for i in range(n):
        feno = randint(1001, 9999)
        fename = faker.name()
        fesal = randint(10000, 200000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
populate(30)
