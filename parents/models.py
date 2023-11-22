from django.db import models
from account.validators.name import validate_name
import datetime
import uuid

class Parents(models.Model):
    parentNo = models.CharField(max_length=20, unique= True)
    fatherName = models.CharField(max_length = 30, null=True,unique=True)
    fatherOccupation = models.CharField(max_length = 30, null=True)
    fatherPhonenumber = models.CharField(max_length = 10, null=True)
    motherName = models.CharField(max_length = 30, null=True,unique=True)
    motherOccupation = models.CharField(max_length = 30, null=True)
    motherPhonenumber = models.CharField(max_length = 10, null=True)
    createdAt = models.DateTimeField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateTimeField(max_length = 30, default=datetime.date.today)