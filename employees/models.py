from django.db import models




   #there are different classes for departments so might as well 
   #seperate them for better usability 
   #foriegn key ensures that if a department is called it must exist
class department(models.Model):
      department = models.CharField(max_length=100)

      # now make sure to make this readable 
      def __str__(self):
         return self.department
      

# Create your models here.
#python wrapper called the ORM
#inherits models.Model which gives us the data base functionality for the model 
#which is like a SQL data base


#charfield requires max length 

#email field can be unique 
class employees(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   phoneNumber= models.CharField(max_length=15)
   address = models.TextField()
   dateOfJoining = models.DateField()
   department = models.ForeignKey(department,on_delete=models.CASCADE)

   def __str__(self):
      return self.name
   

