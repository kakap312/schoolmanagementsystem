from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/core/settings", views.add, name = 'settings'),
    # path("dashboard/class/filter", views.add, name = ''),
    # path("dashboard/class/newentry", views.addParent, name = 'newentryclass'),
    # path("dashboard/class/search", views.searchParent, name = 'searchclass'),
    path("dashboard/settings/delete/<int:id>", views.delete),
    path("dashboard/settings/edit/<int:id>", views.edit, name = 'editclass')
]