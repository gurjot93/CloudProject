from django.db import models

# Create your models here.
class MbrDetails(models.Model):
   mortID =models.AutoField(primary_key=True,default=0)
   username =models.CharField(max_length=100,unique=True)
   password =models.CharField(max_length=100)
   name= models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   number = models.CharField(max_length=100)
   emp_details = models.CharField(max_length=100)
   status = models.CharField(max_length=100,default='pending')

def __str__(self):
   return self.name
