from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/subject/", views.view, name = 'subjectview'), 
    # path("dashboard/fee/filter", views.filter, name = 'filterfee'),
    path("dashboard/subject/newentry", views.add, name = 'newentrysubject'),
    path("dashboard/subject/search", views.search, name = 'searchsubject'),
    path("dashboard/subject/delete/<int:id>", views.delete, name = 'deletesubject'),
    path("dashboard/subject/edit/<int:id>", views.edit, name = 'editsubject')
]


