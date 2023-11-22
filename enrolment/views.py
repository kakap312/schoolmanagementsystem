
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.singleenrolmentform import *
from django.contrib import messages
# from .service import *
from django.db.models import Q
from students.models import *

# Create your views here.

def view(request):
    enrollment = Enrollment.objects.all()
    return render(request,"enrolmentview.html",{'parents':enrollment})

def bulk(request):
    if request.method == "POST":
        class_From = request.POST.get('classfrom')
        year_from = request.POST.get('yearfrom')
        term_from = request.POST.get('termfrom')

        class_to = request.POST.get('classto')
        year_to = request.POST.get('yearto')
        term_to = request.POST.get('termto')

        enrolment = Enrollment.objects.filter(classId = Classes.objects.filter(id = class_From).first(),year = year_from, term = term_from)
        if enrolment:
            for enrol in enrolment:
                if not Enrollment.objects.filter(studentId = enrol.studentId,year = year_to, term = term_to):
                    Enrollment(
                        studentId = enrol.studentId ,
                        classId = Classes.objects.filter(id = class_to).first(),
                        year = year_to,
                        term = term_to
                        ).save()
                else:
                    messages.success(request,f"Students already enrolled for this acdemic year and term.")
                    return render(request,"addbulkenrolment.html",{"classes":Classes.objects.all()})

            
            messages.success(request,f"Enrolment done successfully.")
            return render(request,"addbulkenrolment.html",{"classes":Classes.objects.all()})
        else:
             messages.error(request,f"Sorry no student found in previous class.")
             return render(request,"addbulkenrolment.html",{"classes":Classes.objects.all()})
    else:
        addParentForm = AddEnrolment()
        return render(request,"addbulkenrolment.html",{'form':addParentForm,"classes":Classes.objects.all()})


def single(request):
    if request.method == "POST":
        addParentForm = AddEnrolment(request.POST)
        if addParentForm.is_valid():
             if request.POST.get("id") == "":
                parent = addParentForm.save(commit=False)
                enrolment = Enrollment.objects.filter(studentId = Students.objects.get(id =  int(request.POST.get('studentName'))), year = request.session.get('year'), term = request.session.get('term')).first()
                if enrolment:
                    enrolment.delete()
                parent.studentId = Students.objects.get(id =  int(request.POST.get('studentName')))
                parent.classId =  Classes.objects.get(id = int(request.POST.get('className')))
                parent.year = request.session.get('year')
                parent.term = request.session.get('term')
                parent.save()
                messages.success(request,f"Class has been created Successfully.")
                return render(request,"addsingleenrolment.html",{'form': addParentForm,'students':Students.objects.all(),"classes":Classes.objects.all()})
             else:
                 parent = Enrollment.objects.filter(id = request.POST.get("id")).first()
                 parent.name = addParentForm.cleaned_data['name']
                 parent.save()
                 messages.success(request,f"Fee updated successfully.")
                 return render(request,"addsingleenrolment.html",{'form': addParentForm})
                 
        else:
            return render(request,"addsingleenrolment.html",{'form':addParentForm})

    else:
        addParentForm = AddEnrolment()
        return render(request,"addsingleenrolment.html",{'form':addParentForm,'students':Students.objects.all(),"classes":Classes.objects.all()})


# def add(request):
#     if request.method == "POST":
#         addParentForm = AddEnrolment(request.POST)
#         if addParentForm.is_valid():
#              if request.POST.get("id") == "":
#                 parent = addParentForm.save(commit=False)
#                 id = 0
#                 if Enrollment.objects.all().count() >= 1:
#                     id = Enrollment.objects.all().last().id
#                 if Enrollment.objects.filter(name = addParentForm.cleaned_data['name']):
#                     messages.error(request,f"Sorry!, Fee has been add already.")
#                     return render(request,"addfee.html",{'form': addParentForm})
#                 else:
#                     parent.feeNo = generateParentKey(addParentForm.cleaned_data['name'],id)
#                     parent.save()
#                     messages.success(request,f"Class has been created Successfully.")
#                     return render(request,"addfee.html",{'form': addParentForm})
#              else:
#                  parent = Enrollment.objects.filter(id = request.POST.get("id")).first()
#                  parent.name = addParentForm.cleaned_data['name']
#                  parent.save()
#                  messages.success(request,f"Fee updated successfully.")
#                  return render(request,"addfee.html",{'form': addParentForm})
                 
#         else:
#             return render(request,"addfee.html",{'form':addParentForm})

#     else:
#         addParentForm = AddEnrolment()
#         return render(request,"addfee.html",{'form':addParentForm})
    
# def search(request):
#     searchKey = request.POST.get('searchkey')
#     searchResult  = Enrollment.objects.filter(Q(feeNo = searchKey) | Q(name__startswith = searchKey))
#     return render(request,"feeview.html",{'parents':searchResult})

def delete(request,id):
    enrolment = Enrollment.objects.filter(id = id)
    enrolment.delete()
    enrolment = Enrollment.objects.all()
    return render(request,"enrolmentview.html",{'parents':enrolment})

# def edit(request,id):
#     parent = Enrollment.objects.filter(id = id).first()
#     addParentForm = AddEnrolment(data={
#         "id":parent.id,
#         "name":parent.name,
#         })
#     return render(request,"addfee.html",{'form':addParentForm})

def filter(request):
    if request.method == "POST":
            classId = request.POST.get('classname')
            year = request.session.get('year')
            term = request.session.get('term')
            if  request.POST.get('year') and request.POST.get('term'):
                year = request.POST.get('year')
                term = request.POST.get('term')
            
            enrolment = Enrollment.objects.filter(classId = Classes.objects.filter(id = classId).first() , year = year , term = term)
            if enrolment:
                return render(request,"filterenrolment.html",{"classes":Classes.objects.all(),'parents':enrolment.order_by("studentId__gender")})
            else:
                return render(request,"filterenrolment.html",{"classes":Classes.objects.all()})
    else:
        return render(request,"filterenrolment.html",{"classes":Classes.objects.all()})
