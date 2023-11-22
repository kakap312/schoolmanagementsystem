# from django import forms
# from account.validators.name import validate_name
# from account.models import User
# from django.core.exceptions import ValidationError

# class UserForm(forms.ModelForm):
#     # def clean_firstname(self):
#     #     data = self.cleaned_data.get('firstname')
#     #     validate_name(data)
#     #     return data
        
#     # def clean(self):
#     #     userExist = User.objects.filter(
#     #         firstname = self.cleaned_data.get('firstname'), 
#     #         lastname = self.cleaned_data.get('lastname'),
#     #         middlename = self.cleaned_data.get('middlename')
#     #         ).first()
#     #     if userExist:
#     #         self.add_error('firstname',"Firstname exist")
#     #         self.add_error('lastname',"Lastname exist")
#     #         self.add_error('middlename',"Middlename exist")

#     class Meta:
#         model = User
#         fields = ['firstname','lastname','middlename','phonenumber','dateOfBirth']
#         widgets = {
#             'dateOfBirth': forms.DateInput(attrs={'type':'date'}),
#         }

     


