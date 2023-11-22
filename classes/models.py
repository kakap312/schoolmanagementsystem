from django.db import models
from account.validators.name import validate_name
import datetime
import uuid

class Classes(models.Model):
    classNo = models.CharField(max_length=20, unique= True)
    name = models.CharField(max_length = 30, null=True)
    label = models.CharField(max_length = 30, null=True)
    createdAt = models.DateField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateField(max_length = 30, default=datetime.date.today)