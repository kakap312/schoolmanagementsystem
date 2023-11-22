from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/parents/", views.viewParents, name = 'parentsview'), 
    path("dashboard/parents/filter", views.filterParent, name = 'filter'),
    path("dashboard/parents/newentry", views.addParent, name = 'newentry'),
    path("dashboard/parents/search", views.searchParent, name = 'search'),
    path("dashboard/parents/delete/<int:id>", views.deleteParent, name = 'delete'),
    path("dashboard/parents/edit/<int:id>", views.editParent, name = 'edit')
]