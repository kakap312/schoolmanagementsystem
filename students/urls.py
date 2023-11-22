from django.urls import path 
from .import views

urlpatterns = [
    path("dashboard/students/", views.viewStudents, name ='studentsview'),
    path("dashboard/students/newentry", views.addStudent, name = 'studentnewentry'), 
    path("dashboard/students/search", views.searchStudent, name = 'searchstudent'),
    path("dashboard/students/delete/<int:id>", views.deleteStudent, name = 'deletestudent'),
    path("dashboard/students/edit/<int:id>", views.editStudent, name = 'editstudent'),
    path("dashboard/students/filter", views.filterStudents, name = 'filterstudent'),
    
]