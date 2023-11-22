from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class AddParentForm(forms.ModelForm):
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)

   
    class Meta:
        model = Parents
        fields = ['fatherName','fatherOccupation','fatherPhonenumber','motherName','motherOccupation','motherPhonenumber']
        widgets = {
            'fatherName': forms.TextInput(attrs = {'placeholder':"Firstname Middelname Lastname"}),
             'motherName': forms.TextInput(attrs = {'placeholder':"Firstname Middelname Lastname"}),
            }

     


