from django import forms
from classes.models import *
from subjects.models import *
from ..models import *
from django.core.exceptions import ValidationError

class AssignSubjectForm(forms.Form):
    SUBJECTS = [()]
    CLASSES = [()]
    id = forms.CharField(widget = forms.TextInput(attrs={'type':"hidden",'value':""}),required=False)
    Classes = forms.ChoiceField()
    subject = forms.ChoiceField() 
    
    def __init__(self,*args,**kwargs):
        self.__class__.SUBJECTS.clear()
        self.__class__.CLASSES.clear()
        super(AssignSubjectForm,self).__init__(*args,**kwargs)

        for classes in Classes.objects.all():
            self.__class__.CLASSES.append((classes.id,classes.name))
        for subject in Subjects.objects.all():
            self.__class__.SUBJECTS.append((subject.id,subject.name))
        self.fields['Classes'] = forms.ChoiceField(choices= self.__class__.CLASSES)
        self.fields['subject'] = forms.ChoiceField(choices= self.__class__.SUBJECTS,widget=forms.Select(attrs={"class":"js-example-basic-multiple","multiple":"multiple"}))

    
    field_order = ['Classes','fee_type']

     







