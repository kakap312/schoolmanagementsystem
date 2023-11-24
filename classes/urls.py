from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/class/", views.viewParents, name = 'classview'), 
    path("dashboard/class/filter", views.filterParent, name = 'filterclass'),
    path("dashboard/class/newentry", views.addParent, name = 'newentryclass'),
    path("dashboard/class/search", views.searchParent, name = 'searchclass'),
    path("dashboard/class/assign", views.assignclass, name = 'classassignment'),
    path("dashboard/class/delete/<int:id>", views.deleteParent, name = 'deleteclass'),
    path("dashboard/class/edit/<int:id>", views.editParent, name = 'editclass')
]