from django.db import models

# Create your models here.
class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    mortID = models.CharField(max_length=100,unique=True)

def __str__(self):
    return self.firstName