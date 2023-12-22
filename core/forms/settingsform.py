from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class SettingForm(forms.ModelForm):
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    def clean(self):
        if self.cleaned_data.get('year') <= 0:
            self.add_error('year',"Invalid Input (eg 2001 )")
        if self.cleaned_data.get('term') <= 0:
            self.add_error('term',"Invalid Input (eg 1 )")
        if self.cleaned_data.get('term') > 3:
            self.add_error('term',"Invalid Input (eg 1,2,3 )")
    class Meta:
        model = AcademicSettings
        fields = ['year','term','status']

   
   
   

     


