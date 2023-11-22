from django import forms
from account.validators.name import validate_name
from account.models import Account
from django.core.exceptions import ValidationError

class SigninForm(forms.ModelForm):

   
    class Meta:
        model = Account
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput(),
            }

     
