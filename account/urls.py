
from django.urls import path 
from . import views

urlpatterns = [
    path("signin/", views.signin, name = 'signin'),
    path("signup/", views.signup, name = 'signup'),
    path("userprofile/", views.userprofile, name = 'userprofile'),
    path("dashboard/", views.dashboard, name = 'dashboard'),
    path("recoverpassword/", views.recoverPassword, name = 'recoverpassword')
]