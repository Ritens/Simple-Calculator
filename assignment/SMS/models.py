from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    
    def __str__(self):
      return self.name

