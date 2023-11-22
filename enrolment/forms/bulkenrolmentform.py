from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class AddEnrolment(forms.ModelForm):

    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)

    class Meta:
        model = Enrollment
        fields = []
       
        
    

     


