from django import forms
from account.validators.name import validate_name
from account.models import Account
from classes.models import *
from django.core.exceptions import ValidationError

class BulkBalance(forms.Form):
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    
    # year_from = forms.IntegerField()
    # year_to = forms.IntegerField()
    CLASSES = [()]
    Classes = forms.ChoiceField()
    Balance_Less_Than = forms.IntegerField()

    def __init__(self,*args,**kwargs):
        self.__class__.CLASSES.clear()
        super(BulkBalance,self).__init__(*args,**kwargs)
        for classes in Classes.objects.all():
            self.__class__.CLASSES.append((classes.id,classes.name))
        self.fields['Classes'] = forms.ChoiceField(choices= self.__class__.CLASSES)

   
    

     
