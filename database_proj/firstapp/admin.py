from django.contrib import admin

# Register your models here.

from django.contrib import  admin
from firstapp.models import Employee


# If you want to display more than one column in tree view then uncomment this
#
#
# class employeeAdmin(admin.ModelAdmin):
#     list_display = ['eno','esal']
#
admin.site.register(Employee)
