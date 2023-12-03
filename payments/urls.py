from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/payment/", views.view, name = 'paymentview'), 
    # path("dashboard/fee/filter", views.filter, name = 'filterfee'),
    path("dashboard/payment/receipt/<int:id>", views.receipt),
    path("dashboard/payment/newentry", views.add, name = 'newentrypayment'),
    # path("dashboard/fee/search", views.search, name = 'searchfee'),
    path("dashboard/payment/delete/<int:id>", views.delete),
    # path("dashboard/fee/edit/<int:id>", views.edit, name = 'editfee')
]


