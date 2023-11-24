
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.addclassform import *
from .forms.subjectassignmentform import *
from django.contrib import messages
from .service import *
from django.db.models import Q
from students.models import *

# Create your views here.

def viewParents(request):
    classes = Classes.objects.all()
    return render(request,"classview.html",{'parents':classes})

def addParent(request):
    if request.method == "POST":
        addParentForm = AddClassForm(request.POST)
        if addParentForm.is_valid():
             if request.POST.get("id") == "":
                parent = addParentForm.save(commit=False)
                id = 0
                if Classes.objects.all().count() >= 1:
                    id = Classes.objects.all().last().id
                if Classes.objects.filter(name =addParentForm.cleaned_data['name']).first():
                    messages.error(request,f"Class already exist.")
                    return render(request,"addclass.html",{'form': addParentForm})
                else:
                    parent.classNo = generateParentKey(addParentForm.cleaned_data['label'],id)
                    parent.save()
                    messages.success(request,f"Class has been created Successfully.")
                    return render(request,"addclass.html",{'form': addParentForm})
             else:
                 parent = Classes.objects.filter(id = request.POST.get("id")).first()
                 parent.name = addParentForm.cleaned_data['name']
                 parent.label = addParentForm.cleaned_data['label']
                 parent.save()
                 messages.success(request,f"You Have has been Updated Class.")
                 return render(request,"addclass.html",{'form': addParentForm})
                 
        else:
            return render(request,"addclass.html",{'form':addParentForm})

    else:
        addParentForm = AddClassForm()
        return render(request,"addclass.html",{'form':addParentForm})
    
def assignclass(request):
    if request.method == "POST":
        return 
    else:
        assignClassForm = AssignSubjectForm()
        return render(request,"assignclass.html",{'form':assignClassForm})

    
def searchParent(request):
    searchKey = request.POST.get('searchkey')
    searchResult  = Classes.objects.filter(Q(classNo = searchKey) | Q(name__startswith = searchKey))
    return render(request,"classview.html",{'parents':searchResult})

def deleteParent(request,id):
    parent = Classes.objects.filter(id = id)
    parent.delete()
    parents = Classes.objects.all()
    return render(request,"classview.html",{'parents':parents})

def editParent(request,id):
    parent = Classes.objects.filter(id = id).first()
    addParentForm = AddClassForm(data={
        "id":parent.id,
        "name":parent.name,
        "label":parent.label,
        })
    return render(request,"addclass.html",{'form':addParentForm})

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
