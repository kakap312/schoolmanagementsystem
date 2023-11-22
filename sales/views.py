from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def createSales(request):
     return render(request,"createsales.html",{'formData':'444'})