from django import forms
from ..models import *
from django.core.exceptions import ValidationError

class AddStudentForm(forms.ModelForm):
    Religions = (("Christianity","Christianity"),("Islamic","Islamic"),("Traditional","Traditional"))
    classes = (("Nursery","Nursery"),("Kg1","Kg1"),("Kg2","Kg2"),("P1","P1"),("P2","P2"),("P3","P3"),("P4","P4"),("P5","P5"),("P6","P6"),("JHS1","JHS1"),("JHS2","JHS2"),("JHS3","JHS3"))
    gender = (("Male","Male"),("Female","Female"))
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    religion = forms.ChoiceField(choices=Religions)
    previousSchoolClass =  forms.ChoiceField(choices=classes)
    gender = forms.ChoiceField(choices=gender)
    parentId = forms.CharField(max_length=20)

   
    class Meta:
        model = Students
        fields = ['firstname','middlename','lastname','dob','address','previousSchoolAttended','disability']
        widgets = {
            "dob": forms.DateInput(attrs={'type':'date'})
        }

    def clean(self):
        parentExist = Parents.objects.filter(
            parentNo = self.cleaned_data.get('parentId'), 
            ).first()
        if not parentExist:
            self.add_error('parentId',"Please Parent Id is invalid")

     


