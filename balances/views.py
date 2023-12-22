from django.shortcuts import render
from billing.models import *
from core.models import *
from payments.models import *
from .forms.singlebalance import *
from .forms.bulkbalance import *

# Create your views here.

def single(request):
        singleBalanceForm = SingleBalanceForm(request.POST or None)
       
        if  request.method == "POST" and singleBalanceForm.is_valid():
            totalBills = 0
            totalPayment = 0
            yearsFrom = singleBalanceForm.cleaned_data['year_from']
            yearsTo = singleBalanceForm.cleaned_data['year_to']

            studentBillAndPaymentUiData = []
            billTotalAmountGroupByYear = []
            student = Students.objects.filter(studentNo = singleBalanceForm.cleaned_data['Student_Code']).first()
                
           
            studentBill = Bills.objects.filter(student = student, year__range = (yearsFrom,yearsTo)).order_by('year')
            studentPayment = Payments.objects.filter(student = student, year__range = (yearsFrom,yearsTo)).order_by('year')
            if studentBill or studentPayment:
                tempYears  = studentBill.first().year
                
                for bill in studentBill:
                    if bill.year != tempYears:
                        billTotalAmountGroupByYear.append({'year':tempYears,"billAmount":totalBills})
                        totalBills = 0
                        totalBills += bill.amount
                        tempYears = bill.year
                    elif bill.year == tempYears:
                        totalBills += bill.amount
                        tempYears = bill.year
                   
                for payment in studentPayment:
                    totalPayment += payment.amount
                studentBillAndPaymentUiData.append({'student':student,'bills':billTotalAmountGroupByYear,'paymentAmount':totalPayment})
            return render(request,"singlebalance.html",{'forms':singleBalanceForm, 'balances': studentBillAndPaymentUiData,'bills':billTotalAmountGroupByYear})              
        else:
            return render(request,"singlebalance.html",{'forms': SingleBalanceForm()})

def bulk(request):
    if request.method == "POST":
        return 
    else:
        return render(request,"singlebalance.html",{'forms':BulkBalance()})
