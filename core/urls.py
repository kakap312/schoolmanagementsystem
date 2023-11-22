from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/core/settings", views.add, name = 'settings'),
    # path("dashboard/class/filter", views.add, name = ''),
    # path("dashboard/class/newentry", views.addParent, name = 'newentryclass'),
    # path("dashboard/class/search", views.searchParent, name = 'searchclass'),
    # path("dashboard/class/delete/<int:id>", views.deleteParent, name = 'deleteclass'),
    # path("dashboard/class/edit/<int:id>", views.editParent, name = 'editclass')
]