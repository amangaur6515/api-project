from django.db import models

# Create your models here.

class Member(models.Model):
    FullName=models.CharField(max_length=200)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100)
    MobileNo=models.IntegerField()
    Address=models.CharField(max_length=500)
    Batch=models.CharField(max_length=200)
    JoiningDate=models.DateField()

    def __str__(self):
        return self.FullName
