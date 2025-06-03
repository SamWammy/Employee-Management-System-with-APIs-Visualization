from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from employees.models import employees
# Create your models here.

class performance(models.Model):
    employee = models.ForeignKey(employees, on_delete=models.DO_NOTHING)
    rating = models.IntegerField(
        validators= [
            MinValueValidator(1),
            MaxValueValidator(5)
        ], 
        help_text= "Rating should be between 1 through 5."
    )
    reviewDate= models.DateField()

    def clean(self):
        if self.reviewDate > datetime.date.today():
         raise ValidationError({'reviewDate: review date cannot be in the future'})
