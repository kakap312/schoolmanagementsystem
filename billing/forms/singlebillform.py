from django import forms
from classes.models import *
from fees.models import *
from ..models import *
from django.core.exceptions import ValidationError

class AddSingleBill(forms.ModelForm):
    FEES = [()]
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    student_Id = forms.CharField(max_length=20)
    fee_type = forms.ChoiceField()

    def clean(self):
        studentExist = Students.objects.filter(
            studentNo = self.cleaned_data['student_Id']
            ).first()
        if not studentExist:
            self.add_error('student_Id',"Please Student Id is invalid")
    
    def __init__(self,*args,**kwargs):
        self.__class__.FEES.clear()
        super(AddSingleBill,self).__init__(*args,**kwargs)
        for fee in Fees.objects.all():
            self.__class__.FEES.append((fee.id,fee.name))
        # self.fields['classes'] = forms.ChoiceField(choices= self.__class__.CLASSES)
        self.fields['fee_type'] = forms.ChoiceField(choices= self.__class__.FEES)

    class Meta:
        model = Bills
        fields = ['amount']
        widgets = {
            
            }
    field_order = ['student_Id','fee_type']

    


