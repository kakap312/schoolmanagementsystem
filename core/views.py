from django.shortcuts import render
from .forms.settingsform import *
from django.contrib import messages

# Create your views here.

def add(request):
    # year = 0
    # term = 0
    # if request.session.get('term') or request.session.get(year):
    #         term = request.session.get('term')
    #         year = request.session.get('year')
    settings = AcademicSettings.objects.all()
    if request.method == "POST":
            settingForm = SettingForm(request.POST)
            if settingForm.is_valid():

                searchedSetting = AcademicSettings.objects.filter(year = settingForm.cleaned_data['year'], term = settingForm.cleaned_data['term']).first()
                if request.POST.get("id") == "":
                    if not searchedSetting:
                        if settingForm.cleaned_data['status']:
                            
                            if AcademicSettings.objects.filter(status = settingForm.cleaned_data['status']).first():
                                usedSetting = AcademicSettings.objects.filter(status = settingForm.cleaned_data['status']).first()
                                usedSetting.status = not settingForm.cleaned_data['status']
                                usedSetting.save()
                        settingForm.save()
                        messages.success(request,f"Setting created Successfully")
                        return render(request,"settings.html",{'form':settingForm,'settings':settings})
                    else:
                        messages.error(request,f"Setting creation was  Unsuccessfully")
                        return render(request,"settings.html",{'form':settingForm,})
                else:
                    setting = AcademicSettings.objects.filter(id = int(request.POST.get("id"))).get()
                    setting.year = settingForm.cleaned_data['year']
                    setting.term = settingForm.cleaned_data['term']
                    if settingForm.cleaned_data['status']:
                            if AcademicSettings.objects.filter(status = settingForm.cleaned_data['status']).first():
                                usedSetting = AcademicSettings.objects.filter(status = settingForm.cleaned_data['status']).get()
                                usedSetting.status = not settingForm.cleaned_data['status']
                                usedSetting.save()
                                setting.status = settingForm.cleaned_data['status']

                    setting.status = settingForm.cleaned_data['status']
                    setting.save()
                    messages.success(request,f"Settings updated successfully.")
                    return render(request,"settings.html",{'form': settingForm,'settings':settings})
                     
             
            else:
                 return render(request,"settings.html",{'form':settingForm,'settings':settings})
    else:
        settingForm = SettingForm()
        return render(request,"settings.html",{'form':settingForm,'settings':settings})
    
def delete(request,id):
    settingForm = SettingForm()
    settings = AcademicSettings.objects.filter(id = id)
    settings.delete()
    settings = AcademicSettings.objects.all()
    return render(request,"settings.html",{'form':settingForm , 'settings':settings})

def edit(request,id):
    setting = AcademicSettings.objects.filter(id = id).first()
    addSettingForm = SettingForm(data={
        "id":setting.id,
        "year":setting.year,
        "term": setting.term,
        "status": setting.status
        })
    return render(request,"settings.html",{'form':addSettingForm,'settings':AcademicSettings.objects.all()})
