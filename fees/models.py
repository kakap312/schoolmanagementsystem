from django.db import models
from account.validators.name import validate_name
import datetime
import uuid

class Fees(models.Model):
    feeNo = models.CharField(max_length=20, unique= True)
    name = models.CharField(max_length = 30, null=True)
    # amount = models.DecimalField(max_length = 30, null=True,decimal_places=2,max_digits=1000)
    createdAt = models.DateField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateField(max_length = 30, default=datetime.date.today)