from django.db import models
from students.models import *
from classes.models import *

# Create your models here.

class Enrollment(models.Model):
    studentId = models.ForeignKey(to=Students, on_delete=models.CASCADE,unique=False,null=True)
    classId = models.ForeignKey(to=Classes,on_delete=models.CASCADE,unique=False,null=True)
    year = models.IntegerField()
    term = models.IntegerField()
    createdAt = models.DateField(max_length = 30, default=datetime.date.today)
    updatedAt = models.DateField(max_length = 30, default=datetime.date.today)
