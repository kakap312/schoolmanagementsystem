
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.addfeesform import *
from django.contrib import messages
from .service import *
from django.db.models import Q
from students.models import *

# Create your views here.

def view(request):
    subjects = Subjects.objects.all()
    return render(request,"subjectview.html",{'parents':subjects})

def add(request):
    if request.method == "POST":
        addParentForm = AddSubjectForm(request.POST)
        if addParentForm.is_valid():
             if request.POST.get("id") == "":
                parent = addParentForm.save(commit=False)
                id = 0
                if Subjects.objects.all().count() >= 1:
                    id = Subjects.objects.all().last().id
                if Subjects.objects.filter(name = addParentForm.cleaned_data['name']):
                    messages.error(request,f"Sorry!, Fee has been add already.")
                    return render(request,"addsubject.html",{'form': addParentForm})
                else:
                    parent.subjectNo = generateParentKey(addParentForm.cleaned_data['name'],id)
                    parent.save()
                    messages.success(request,f"Subject has been created Successfully.")
                    return render(request,"addsubject.html",{'form': addParentForm})
             else:
                 parent = Subjects.objects.filter(id = request.POST.get("id")).first()
                 parent.name = addParentForm.cleaned_data['name']
                 parent.save()
                 messages.success(request,f"Fee updated successfully.")
                 return render(request,"addsubject.html",{'form': addParentForm})
                 
        else:
            return render(request,"addsubject.html",{'form':addParentForm})

    else:
        addParentForm = AddSubjectForm()
        return render(request,"addsubject.html",{'form':addParentForm})
    
# def search(request):
#     searchKey = request.POST.get('searchkey')
#     searchResult  = Fees.objects.filter(Q(feeNo = searchKey) | Q(name__startswith = searchKey))
#     return render(request,"feeview.html",{'parents':searchResult})

# def delete(request,id):
#     parent = Fees.objects.filter(id = id)
#     parent.delete()
#     parents = Fees.objects.all()
#     return render(request,"feeview.html",{'parents':parents})

# def edit(request,id):
#     parent = Fees.objects.filter(id = id).first()
#     addParentForm = AddFeesForm(data={
#         "id":parent.id,
#         "name":parent.name,
#         })
#     return render(request,"addfee.html",{'form':addParentForm})

# def filter(request):
#     searchKey = request.POST.get('searchkey')
#     if searchKey:
#         parent  = Parents.objects.filter(parentNo = searchKey).first()
#         if parent:
#             students = Students.objects.filter(parentId = parent.id)
#             return render(request,"filterparent.html",{'parent':parent,'students':students}) 
#         else:
#              return render(request,"filterparent.html",{'parent':parent})    
#     else:
#         return render(request,"filterparent.html")
