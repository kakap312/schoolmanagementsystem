from django import forms
from classes.models import *
from fees.models import *
from ..models import *
from django.core.exceptions import ValidationError

class AddBulkBill(forms.ModelForm):
    FEES = [()]
    CLASSES = [()]
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    Classes = forms.ChoiceField()
    fee_type = forms.ChoiceField()
    
    def __init__(self,*args,**kwargs):
        self.__class__.FEES.clear()
        self.__class__.CLASSES.clear()
        super(AddBulkBill,self).__init__(*args,**kwargs)

        for classes in Classes.objects.all():
            self.__class__.CLASSES.append((classes.id,classes.name))
        for fee in Fees.objects.all():
            self.__class__.FEES.append((fee.id,fee.name))
        self.fields['Classes'] = forms.ChoiceField(choices= self.__class__.CLASSES)
        self.fields['fee_type'] = forms.ChoiceField(choices= self.__class__.FEES)

    class Meta:
        model = Bills
        fields = ['amount']
        widgets = {
            
            }
    field_order = ['Classes','fee_type']

     


