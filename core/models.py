from django.db import models
import datetime

# Create your models here.
class AcademicSettings(models.Model):
    year = models.PositiveIntegerField( null=True)
    term = models.PositiveIntegerField(null=True)
    status = models.BooleanField(max_length = 15,default=False)
    createdAt = models.DateField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateField(max_length = 30, default=datetime.date.today)
