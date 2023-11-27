from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class SettingForm(forms.Form):
    academicYear = forms.IntegerField(required=True)
    term = forms.IntegerField(max_value=3,)

    def clean(self):
        if self.cleaned_data.get('academicYear') <= 0:
            self.add_error('academicYear',"Invalid Input (eg 2001 )")
        if self.cleaned_data.get('term') <= 0:
            self.add_error('term',"Invalid Input (eg 1 )")


   
   

     


