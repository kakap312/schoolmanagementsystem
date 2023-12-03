from django.db import models
from students.models import *

class Payments (models.Model):
    paymentNo = models.CharField(max_length=20, unique= True)
    student = models.ForeignKey(to = Students, on_delete= models.CASCADE)
    amount = models.DecimalField(decimal_places= 2, max_digits=10000, null=True)
    year = models.PositiveIntegerField(null=True)
    term = models.PositiveIntegerField(null=True)
    createdAt = models.DateField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateField(max_length = 30, default=datetime.date.today)
