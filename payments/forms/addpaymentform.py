from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class AddPAymentForm(forms.ModelForm):
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    student_Id = forms.CharField(max_length=20)

    def clean(self):
        studentExist = Students.objects.filter(
            studentNo = self.cleaned_data['student_Id']
            ).first()
        if not studentExist:
            self.add_error('student_Id',"Please Student Id is invalid")
   
    class Meta:
        model = Payments
        fields = ['amount']

    field_order = ['student_Id','amount']
        

     


