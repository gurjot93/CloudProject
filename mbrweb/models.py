from django.db import models

# Create your models here.
class MbrDetails(models.Model):
   mortID =models.CharField(max_length=100,unique=True)
   username =models.CharField(max_length=100,unique=True)
   password =models.CharField(max_length=100,default='test')
   name= models.CharField(max_length=100,default='test')
   address = models.CharField(max_length=100,default='test')
   number = models.CharField(max_length=100,default='test')
   emp_details = models.CharField(max_length=100,default='test')
   status = models.CharField(max_length=100,default='pending')

def __str__(self):
   return self.name
