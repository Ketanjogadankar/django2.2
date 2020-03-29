import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','database_proj.settings')
import django
django.setup()

from firstapp.models import *
from faker import  Faker
from random import *
faker = Faker()

def phonenumbergen( ):
    number = randint(7,9)
    num_str = ''+str(number)
    for i in range(0,9):
        num_str = num_str+str(randint(0,9))
    return int(num_str)


def populate(n):
    for i in range(n):
        feno = randint(1001, 9999)
        fename = faker.name()
        fesal = randint(10000, 200000)
        feaddr = faker.city()
        fephonenum = phonenumbergen()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr,phonnum=fephonenum )
populate(30)
