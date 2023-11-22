from django.shortcuts import render
from .forms.settingsform import *
from django.contrib import messages

# Create your views here.

def add(request):
    
    if request.method == "POST":
            settingForm = SettingForm(request.POST)
            if settingForm.is_valid():
                request.session['year'] = settingForm.cleaned_data['academicYear']
                request.session['term'] = settingForm.cleaned_data['term']
                messages.success(request,f"Setting created Successfully")
                return render(request,"settings.html",{'form':settingForm})
            else:
                 return render(request,"settings.html",{'form':settingForm})
    else:
        settingForm = SettingForm()
        return render(request,"settings.html",{'form':settingForm})