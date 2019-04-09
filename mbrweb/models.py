from django.db import models

# Create your models here.
class MbrDetails(models.Model):
   name= models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   number = models.CharField(max_length=100)
   emp_details = models.CharField(max_length=100)
   status = models.CharField(max_length=100,default='pending')

def __str__(self):
   return self.name
