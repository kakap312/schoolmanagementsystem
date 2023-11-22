
from django import forms

def validate_name(value):
    if len(value) > 8:
        raise forms.ValidationError("Username Must be eight(8) digits")
    elif(len(value) < 1):
        raise forms.ValidationError("Please type in your username")