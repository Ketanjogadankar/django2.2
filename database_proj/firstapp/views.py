from django.shortcuts import render
from firstapp.models import Employee

# Create your views here.

def employee_info_view(request):
    # employees = Employee.objects.all()
    # employees = Employee.objects.all().order_by('ename')
    employees = Employee.objects.all().order_by('-eno')  #order bu desending order
    # employees = Employee.objects.filter(eno__lt=4000)  #django ORM code
    # employees = Employee.objects.filter(ename__startswith='S')  #django ORM code
    return  render(request, 'testapp/results.html',{'employees':employees})
