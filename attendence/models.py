from django.db import models
from employees.models import employees


class attendence(models.Model):
    statusChoices= [
        ("present","Present"),
        ("absent", "Absent"),
        ("late", "Late"),
       ]
    #employee name foreign key must take a model so im just gonna give it the entire employee details, its fk anyway so it doesnt really matter
    employeeName = models.ForeignKey(employees,on_delete=models.DO_NOTHING)
    date = models.DateField()
    status= models.CharField(max_length=10, choices=statusChoices)


    def __str__(self):
        return self.employeeName
# Create your models here.
