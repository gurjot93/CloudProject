from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name= models.CharField(max_length=100,default='test')
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100,default='test')
    salary = models.CharField(max_length=100,default='test')
    startDate = models.CharField(max_length=100,default='test')

def __str__(self):
    return self.firstName