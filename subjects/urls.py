from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/subject/", views.view, name = 'subjectview'), 
    # path("dashboard/fee/filter", views.filter, name = 'filterfee'),
    path("dashboard/subject/newentry", views.add, name = 'newentrysubject'),
    # path("dashboard/fee/search", views.search, name = 'searchfee'),
    # path("dashboard/fee/delete/<int:id>", views.delete, name = 'deleteclass'),
    # path("dashboard/fee/edit/<int:id>", views.edit, name = 'editfee')
]


