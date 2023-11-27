from django.shortcuts import render
from .forms.settingsform import *
from django.contrib import messages

# Create your views here.

def add(request):
    year = 0
    term = 0
    if request.session.get('term') or request.session.get(year):
            term = request.session.get('term')
            year = request.session.get('year')
    
    if request.method == "POST":
            settingForm = SettingForm(request.POST)
            if settingForm.is_valid():
                request.session['year'] = settingForm.cleaned_data['academicYear']
                request.session['term'] = settingForm.cleaned_data['term']
                messages.success(request,f"Setting created Successfully")
                return render(request,"settings.html",{'form':settingForm,'term':request.session.get('term'),'year':request.session.get('year')})
            else:
                 return render(request,"settings.html",{'form':settingForm,'term':term,'year':year})
    else:
        settingForm = SettingForm()
        
        return render(request,"settings.html",{'form':settingForm,'term':term,'year':year})