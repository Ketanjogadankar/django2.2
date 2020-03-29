from django.contrib import admin


from django.contrib import  admin
from appdjango.models import Employee


class employeeAdmin(admin.ModelAdmin):
    list_display = ['eno','esal']

admin.site.register(Employee,employeeAdmin)


# Register your models here.
