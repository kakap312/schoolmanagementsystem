
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.singlebillform import *
from .forms.bulkbillform import *
from .service import *
from enrolment.models import *
from django.contrib import messages
from django.db.models import Q
from students.models import *

# Create your views here.

def view(request):
    bill = Bills.objects.all()
    return render(request,"billview.html",{'parents':bill})

def add(request):
    if request.method == "POST":
        addStudentForm = AddSingleBill(request.POST)
        if addStudentForm.is_valid():
            student = Students.objects.filter(studentNo = addStudentForm.cleaned_data['student_Id']).first()
            fee = Fees.objects.filter(id = addStudentForm.cleaned_data['fee_type']).first()
            if request.POST.get("id") == "":
                
                if Bills.objects.filter(student=student,fees=fee,year=request.session.get('year'),term = request.session.get('term')).first():
                    messages.success(request,f"bill  already exist.")
                    return render(request,"addbill.html",{'form': addStudentForm})
                else:
                    bill = Bills()
                    bill.student = student
                    bill.fees = fee
                    bill.year = request.session.get('year')
                    bill.billNo = generateParentKey(Bills.objects.count())
                    bill.term = request.session.get('term')
                    bill.amount = addStudentForm.cleaned_data['amount']
                    bill.save()
                    messages.success(request,f"bill  has been created Successfully.")
                    return render(request,"addbill.html",{'form': addStudentForm})
            else:
                 bill = Bills.objects.filter(student=student,fees=fee,year=request.session.get('year'),term = request.session.get('term')).first()
                 if bill:
                    bill.student = student
                    bill.fees = fee
                    bill.amount = addStudentForm.cleaned_data['amount']
                    bill.save()
                    messages.success(request,f"Bill updated successfully.")
                    return render(request,"addbill.html",{'form': AddSingleBill(request.POST)}) 
                 else:
                    bill = Bills.objects.filter(id = addStudentForm.cleaned_data['id']).first()
                    bill.student = student
                    bill.fees = fee
                    bill.amount = addStudentForm.cleaned_data['amount']
                    bill.save()
                    messages.success(request,f"Bill updated successfully.")
                    return render(request,"addbill.html",{'form': AddSingleBill(request.POST)})     
        else:
            return render(request,"addbill.html",{'form':AddSingleBill(request.POST)})
    else:
        addParentForm = AddSingleBill()
        return render(request,"addbill.html",{'form':addParentForm})

def bulk(request):
    if request.method == "POST":
        addBulkForm = AddBulkBill(request.POST)
        if addBulkForm.is_valid():
            classes = Classes.objects.filter(id = addBulkForm.cleaned_data['Classes']).first()
            fee = Fees.objects.filter(id = addBulkForm.cleaned_data['fee_type']).first()
            enrolment = Enrollment.objects.filter(classId = classes,year = request.session.get('year'),term = request.session.get('term'))
            if enrolment:
                for enrol in enrolment:
                    if not Bills.objects.filter(student=enrol.studentId,fees=fee,year=request.session.get('year'),term = request.session.get('term')).first():
                        bill = Bills()
                        bill.student = enrol.studentId
                        bill.fees = fee
                        bill.year = request.session.get('year')
                        bill.billNo = generateParentKey(Bills.objects.count())
                        bill.term = request.session.get('term')
                        bill.amount = addBulkForm.cleaned_data['amount']
                        bill.save()
                messages.success(request,f"Bill Created successfully.")
                return render(request,"addbulkbill.html",{'form':addBulkForm})
            else:
                messages.error(request,f" Sorry! No Student Found in the selected class")
                return render(request,"addbulkbill.html",{'form':addBulkForm})
        else:
            return render(request,"addbill.html",{'form':addBulkForm})

    else:
        addParentForm = AddBulkBill()
        return render(request,"addbulkbill.html",{'form':addParentForm})

    
# def search(request):
#     searchKey = request.POST.get('searchkey')
#     searchResult  = Fees.objects.filter(Q(feeNo = searchKey) | Q(name__startswith = searchKey))
#     return render(request,"feeview.html",{'parents':searchResult})

def delete(request,id):
    bill = Bills.objects.filter(id = id)
    bill.delete()
    bills = Bills.objects.all().order_by("createdAt")
    return render(request,"billview.html",{'parents':bills})

def edit(request,id):
    bill = Bills.objects.filter(id = id).first()
    addParentForm = AddSingleBill(data={
        "id":bill.id,
        "student_Id":bill.student.studentNo,
        "amount":bill.amount,
        "fee_type":bill.fees.id
        })
    return render(request,"addbill.html",{'form':addParentForm})

def search(request):
    searchKey = request.POST.get('searchkey')
    if searchKey:
        filteedStudent = Students.objects.filter(Q(studentNo = searchKey) | Q(firstname__contains = searchKey) | Q(lastname__contains = searchKey) | Q(middlename__contains = searchKey)).first()
        searchResult  = Bills.objects.filter(Q(billNo = searchKey) | Q(student = filteedStudent))
        return render(request,"billview.html",{'parents':searchResult})
    else:
        return render(request,"feeview.html")

def filter(request):
    if request.method == "POST":
            classId = request.POST.get('classname')
            year = request.session.get('year')
            term = request.session.get('term')
            if  request.POST.get('year') and request.POST.get('term'):
                year = request.POST.get('year')
                term = request.POST.get('term')
            bills = []
            totalAmount=0
            enrolment = Enrollment.objects.filter(classId = Classes.objects.filter(id = classId).first() , year = year , term = term)
            if enrolment:
                for enrol in enrolment:
                    bill = Bills.objects.filter(student = enrol.studentId,year = year,term=term).all()
                    if  bill:
                        for bil in bill:
                            bills.append(bil)
                            totalAmount+= bil.amount
                return render(request,"filterbill.html",{"classes":Classes.objects.all(),'parents':bills,'totalamount':totalAmount})
            else:
                return render(request,"filterbill.html",{"classes":Classes.objects.all()})
    else:
        return render(request,"filterbill.html",{"classes":Classes.objects.all()})
