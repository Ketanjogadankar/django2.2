from django.db import models

# Create your models here.
# username:mayur200
# emailid:mayur.pardeshi96@gmail.com
# pass:aai123

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=40)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)


    def __str__(self):
        return self.ename
