from django.db import models
from account.validators.name import validate_name
import datetime
import uuid

# Create your models here.

# class User(models.Model):
#     userKey = models.UUIDField(primary_key=False,editable=False,unique=True,default=uuid.uuid4)
#     firstname = models.CharField(max_length = 15, unique=True)
#     middlename = models.CharField(max_length = 15)
#     lastname = models.CharField(max_length = 100)
#     phonenumber = models.IntegerField()
#     dateOfBirth = models.DateTimeField(max_length = 30, auto_created=True)
  

class Account(models.Model):
    username = models.CharField(max_length = 8)
    password = models.CharField(max_length = 8)
    securityQuestion = models.CharField(max_length = 100)
    state = models.CharField(max_length=10)
    firstname = models.CharField(max_length = 15, null=True)
    middlename = models.CharField(max_length = 15,null=True)
    lastname = models.CharField(max_length = 100, null= True)
    phonenumber = models.CharField(max_length= 10, null= True)
    dateOfBirth = models.DateTimeField(max_length = 30, null= True)
    # owner = models.ForeignKey(to=User, on_delete= models.CASCADE)
    created_At = models.DateField(max_length = 50, default=datetime.date.today)
    updated_At = models.DateField(max_length = 50,default=datetime.date.today)



