from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/bill/", views.view, name = 'billview'), 
    path("dashboard/bill/filter", views.filter, name = 'filterbill'),
    path("dashboard/bill/newentry", views.add, name = 'newentrysinglebill'),
    path("dashboard/bill/newentrybulk", views.bulk, name = 'newentrybulkbill'),
    path("dashboard/bill/search", views.search, name = 'searchbill'),
    path("dashboard/bill/delete/<int:id>", views.delete, name = 'deletebill'),
    path("dashboard/bill/edit/<int:id>", views.edit, name = 'editbill')
]


