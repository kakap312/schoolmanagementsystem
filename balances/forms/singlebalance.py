from django import forms
from account.validators.name import validate_name
from account.models import Account
from students.models import Students
from django.core.exceptions import ValidationError

class SingleBalanceForm(forms.Form):
    Student_Code = forms.CharField(max_length=20)
    year_from = forms.IntegerField()
    year_to = forms.IntegerField()

   
def clean(self):
        studentExist = Students.objects.filter(
            studentNo = self.cleaned_data['Student_Code'], 
            ).first()
        if not studentExist:
            self.add_error('Student_Code',"Please Parent Id is invalid")

     
