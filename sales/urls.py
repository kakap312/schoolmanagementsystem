
from django.urls import path 
from . import views

urlpatterns = [
    path("sale/", views.createSales)
]