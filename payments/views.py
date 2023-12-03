
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms.addpaymentform import *
from django.contrib import messages
from .service import *
from django.db.models import Q
from students.models import *
from billing.models import *
from num2words import num2words

# Create your views here.

def view(request):
    payments = Payments.objects.all()
    return render(request,"paymentview.html",{'payments':payments})

def add(request):
    if request.method == "POST":
        addPaymentForm = AddPAymentForm(request.POST)
        if addPaymentForm.is_valid():
             if request.POST.get("id") == "":
                payment = addPaymentForm.save(commit=False)                                                                                                                                            
                payment.paymentNo = generateKey(Payments.objects.all().count())
                payment.amount = addPaymentForm.cleaned_data['amount']
                payment.year = request.session.get('year')
                payment.term = request.session.get('term')
                payment.student = Students.objects.filter(studentNo = addPaymentForm.cleaned_data['student_Id']).first()
                payment.save()
                messages.success(request,f"Payment has been created Successfully.")
                return render(request,"addpayment.html",{'form': addPaymentForm})
             else:
                 payment = Payments.objects.filter(id = request.POST.get("id")).first()
                 payment.amount = addPaymentForm.cleaned_data['name']
                 payment.student = Students.objects.filter(studentNo = addPaymentForm.cleaned_data['student_Id']).first()
                 payment.updatedAt = datetime.datetime.date
                 payment.save()
                 messages.success(request,f"Payment updated successfully.")
                 return render(request,"addpayment.html",{'form': addPaymentForm})
                 
        else:
            return render(request,"addpayment.html",{'form':addPaymentForm})

    else:
        addPaymentForm = AddPAymentForm()
        return render(request,"addpayment.html",{'form':addPaymentForm})
    
def receipt(request,id):
    totalPayment = 0;
    totalBill = 0
    student =  Payments.objects.filter(id = id).first().student
    payments = Payments.objects.filter(student = student ,year = request.session.get('year'), term = request.session.get('term')).all()
    for payment in payments:
        totalPayment += payment.amount
    bills = Bills.objects.filter(student = student , year = request.session.get('year'), term = request.session.get('term')).all()
    for bill in bills:
        totalBill += bill.amount

    areas = totalBill - totalPayment
    balance = totalBill - totalPayment
    if areas < 0:
        areas = 0
        balance = balance
    else:
        areas = areas
        balance = 0

   
    return render(request,"paymentreceipt.html",{'term':request.session.get('term'),"year":request.session.get('year'),'student':student,"payment" : Payments.objects.filter(id = id).first(),"word":num2words(Payments.objects.filter(id = id).first().amount),"areas":areas,"balance":balance})
    
    
# def search(request):
#     searchKey = request.POST.get('searchkey')
#     searchResult  = Fees.objects.filter(Q(feeNo = searchKey) | Q(name__startswith = searchKey))
#     return render(request,"feeview.html",{'payments':searchResult})

def delete(request,id):
    payment = Payments.objects.filter(id = id)
    payment.delete()
    payments = Payments.objects.all()
    return render(request,"paymentview.html",{'payments':payments})

# def edit(request,id):
#     payment = Fees.objects.filter(id = id).first()
#     addPaymentForm = AddFeesForm(data={
#         "id":payment.id,
#         "name":payment.name,
#         })
#     return render(request,"addfee.html",{'form':addPaymentForm})

# def filter(request):
#     searchKey = request.POST.get('searchkey')
#     if searchKey:
#         payment  = payments.objects.filter(paymentNo = searchKey).first()
#         if payment:
#             students = Students.objects.filter(paymentId = payment.id)
#             return render(request,"filterpayment.html",{'payment':payment,'students':students}) 
#         else:
#              return render(request,"filterpayment.html",{'payment':payment})    
#     else:
#         return render(request,"filterpayment.html")
