
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.addparentForm import *
from django.contrib import messages
from .service import *
from django.db.models import Q
from students.models import *

# Create your views here.

def viewParents(request):
    parents = Parents.objects.all()
    return render(request,"parentsview.html",{'parents':parents})

def addParent(request):
    if request.method == "POST":
        addParentForm = AddParentForm(request.POST)
        if addParentForm.is_valid():
             if request.POST.get("id") == "":
                parent = addParentForm.save(commit=False)
                namePartList = addParentForm.cleaned_data['fatherName'].split()
                parent.parentNo = generateParentKey(namePartList,Parents.objects.count())
                parent.save()
                messages.success(request,f"Parent  has been created Successfully.")
                return render(request,"addparent.html",{'form': addParentForm})
             else:
                 namePartList = addParentForm.cleaned_data['fatherName'].split()
                 parent = Parents.objects.filter(id = request.POST.get("id")).first()
                 parent.fatherName = addParentForm.cleaned_data['fatherName']
                 parent.fatherOccupation = addParentForm.cleaned_data['fatherOccupation']
                 parent.fatherPhonenumber = addParentForm.cleaned_data['fatherPhonenumber']
                 parent.motherName = addParentForm.cleaned_data['motherName']
                 parent.motherOccupation = addParentForm.cleaned_data['motherOccupation']
                 parent.motherPhonenumber = addParentForm.cleaned_data['motherPhonenumber']
                 parent.parentNo = generateParentKey(namePartList,request.POST.get("id"),update=True)
                 parent.save()
                 messages.success(request,f"You Have has been Updated Parent.")
                 return render(request,"addparent.html",{'form': addParentForm})
                 
        else:
            return render(request,"addparent.html",{'form':addParentForm})

    else:
        addParentForm = AddParentForm()
        return render(request,"addparent.html",{'form':addParentForm})
    
def searchParent(request):
    searchKey = request.POST.get('searchkey')
    searchResult  = Parents.objects.filter(Q(parentNo = searchKey) | Q(fatherName__startswith = searchKey) | Q(motherName__startswith = searchKey))
    return render(request,"parentsview.html",{'parents':searchResult})

def deleteParent(request,id):
    parent = Parents.objects.filter(id = id)
    parent.delete()
    parents = Parents.objects.all()
    return render(request,"parentsview.html",{'parents':parents})

def editParent(request,id):
    parent = Parents.objects.filter(id = id).first()
    addParentForm = AddParentForm(data={
        "id":parent.id,
        "fatherName":parent.fatherName,
        "fatherOccupation":parent.fatherOccupation,
        "fatherPhonenumber":parent.fatherPhonenumber,
        "motherName":parent.motherName,
        "motherOccupation":parent.motherOccupation,
        "motherPhonenumber":parent.motherPhonenumber,
        
        })
    return render(request,"addparent.html",{'form':addParentForm})

def filterParent(request):
    searchKey = request.POST.get('searchkey')
    if searchKey:
        parent  = Parents.objects.filter(parentNo = searchKey).first()
        if parent:
            students = Students.objects.filter(parentId = parent.id)
            return render(request,"filterparent.html",{'parent':parent,'students':students}) 
        else:
             return render(request,"filterparent.html",{'parent':parent})    
    else:
        return render(request,"filterparent.html")
