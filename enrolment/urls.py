from django.urls import path 
from . import views

urlpatterns = [
    path("dashboard/enrolment/", views.view, name = 'enrolview'), 
    path("dashboard/enrolment/filter", views.filter, name = 'filterenrolment'),
    path("dashboard/enrolment/newentry", views.single, name = 'newentrysingle'),
    path("dashboard/enrolment/newentrybulk", views.bulk, name = 'newentrybulk'),
    # path("dashboard/class/search", views.searchParent, name = 'searchclass'),
    path("dashboard/enrol/delete/<int:id>", views.delete, name = 'deleteenrolment'),
    # path("dashboard/class/edit/<int:id>", views.editParent, name = 'editclass')
]