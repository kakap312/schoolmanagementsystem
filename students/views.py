
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.addstudentform import *
from django.contrib import messages
from django.db.models import Q
from students.models import *
from .service import *
import datetime
from enrolment.models import *


# Create your views here.

def viewStudents(request):
    students = Students.objects.all()
    return render(request,"studentview.html",{'students':students,'currentyear':datetime.date.today().year})

def addStudent(request):
    if request.method == "POST":
        addStudentForm = AddStudentForm(request.POST)
        if addStudentForm.is_valid():
             studentParent = Parents.objects.filter(parentNo = addStudentForm.cleaned_data['parentId'] ).first()
             if request.POST.get("id") == "":
                namePartList = [addStudentForm.cleaned_data['firstname'],addStudentForm.cleaned_data['middlename'],addStudentForm.cleaned_data['lastname']]
                studentNo = generateParentKey(namePartList,Students.objects.count())
                student = Students(
                    firstname = addStudentForm.cleaned_data['firstname'],
                    middlename = addStudentForm.cleaned_data['middlename'],
                    lastname = addStudentForm.cleaned_data['lastname'],
                    gender = addStudentForm.cleaned_data['gender'],
                    dob = addStudentForm.cleaned_data['dob'],
                    address = addStudentForm.cleaned_data['address'],
                    religion = addStudentForm.cleaned_data['religion'],
                    previousSchoolClass = addStudentForm.cleaned_data['previousSchoolClass'],
                    previousSchoolAttended = addStudentForm.cleaned_data['previousSchoolAttended'],
                    parentId = studentParent,
                    studentNo = studentNo,
                    disability = addStudentForm.cleaned_data['disability']
                )
                student.save()
                messages.success(request,f"Student  has been created Successfully.")
                return render(request,"addparent.html",{'form': addStudentForm})
             else:
                 student = Students.objects.filter(id = request.POST.get("id")).first()
                 student.firstname = addStudentForm.cleaned_data['firstname']
                 student.middlename = addStudentForm.cleaned_data['middlename']
                 student.lastname = addStudentForm.cleaned_data['lastname']
                 student.gender = addStudentForm.cleaned_data['gender']
                 student.dob = addStudentForm.cleaned_data['dob']
                 student.address = addStudentForm.cleaned_data['address']
                 student.religion = addStudentForm.cleaned_data['religion']
                 student.previousSchoolClass = addStudentForm.cleaned_data['previousSchoolClass']
                 student.parentId = studentParent
                 student.disability = addStudentForm.cleaned_data['disability']
                 student.save()
                 messages.success(request,f"You Have has been Updated Student.")
                 return render(request,"addstudent.html",{'form': addStudentForm})      
        else:
            return render(request,"addstudent.html",{'form':addStudentForm})

    else:
        addStudentForm = AddStudentForm()
        return render(request,"addstudent.html",{'form':addStudentForm})
  
def searchStudent(request):
    selectedStudents = []
    searchKey = request.POST.get('searchkey').strip()
    try:
        if int(searchKey):
            students = Students.objects.all()
            for student in students:
                if (datetime.date.today().year - student.dob.year) == int(searchKey):
                    selectedStudents.append(student)
            return render(request,"studentview.html",{'students':selectedStudents,'currentyear':datetime.date.today().year})
    except:
        searchResult  = Students.objects.filter(Q(studentNo = searchKey) | Q(firstname__contains = searchKey) | Q(lastname__contains = searchKey) | Q(middlename__contains = searchKey))
        return render(request,"studentview.html",{'students':searchResult,'currentyear':datetime.date.today().year})      

    

def deleteStudent(request,id):
    student = Students.objects.filter(id = id)
    student.delete()
    students = Students.objects.all()
    return render(request,"studentview.html",{'students':students, 'currentyear':datetime.date.today().year})

def editStudent(request,id):
    student = Students.objects.filter(id = id).first()
    parent = Parents.objects.filter(id = student.parentId.id).first()
    addParentForm = AddStudentForm(data={
        "id":student.id,
        "firstname" : student.firstname,
        "lastname":student.lastname,
        "middlename" : student.middlename,
        "gender":student.gender,
        "dob":student.dob,
        "address":student.address,
        "previousSchoolClass":student.previousSchoolClass,
        "religion":student.religion,
        "previousSchoolAttended":student.previousSchoolAttended,
        "parentId" : parent.parentNo,
        "disability": student.disability
        })
    return render(request,"addstudent.html",{'form':addParentForm})


def filterStudents(request):
    if request.method == "POST":
        searchKey = request.POST.get('searchkey')
        classes = Classes.objects.filter(name = searchKey).first()
        enrolment = Enrollment.objects.filter(classId = classes , year= request.session.get('year'),term = request.session.get('term'))
        return render(request,"filterstudent.html",{'students':enrolment.order_by("studentId__gender")})
    else:
        return render(request,"filterstudent.html")


