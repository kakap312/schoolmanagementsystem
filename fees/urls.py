from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/fee/", views.view, name = 'feeview'), 
    path("dashboard/fee/filter", views.filter, name = 'filterfee'),
    path("dashboard/fee/newentry", views.add, name = 'newentryfee'),
    path("dashboard/fee/search", views.search, name = 'searchfee'),
    path("dashboard/fee/delete/<int:id>", views.delete, name = 'deleteclass'),
    path("dashboard/fee/edit/<int:id>", views.edit, name = 'editfee')
]


