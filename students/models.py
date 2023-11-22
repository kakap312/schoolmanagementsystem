from django.db import models
from account.validators.name import validate_name
import datetime
import uuid
from parents.models import *

class Students(models.Model):
    studentNo = models.CharField(max_length=20, unique= True)
    parentId = models.ForeignKey(to=Parents, on_delete= models.CASCADE)
    firstname = models.CharField(max_length = 15, null=True)
    middlename = models.CharField(max_length = 15, null=True)
    lastname = models.CharField(max_length = 15, null=True)
    dob = models.DateField(max_length = 30, null=True)
    address =  models.CharField(max_length = 15, null=True)
    gender =  models.CharField(max_length = 5, null=True)
    nationality =  models.CharField(max_length = 15, null=True, default="Ghanaian")
    religion =  models.CharField(max_length = 15, null=True)
    previousSchoolAttended = models.CharField(max_length = 20, null=True)
    previousSchoolClass = models.CharField(max_length = 10, null=True)
    disability = models.CharField(max_length = 20, null=True)
    createdAt = models.DateField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateField(max_length = 30, default=datetime.date.today)