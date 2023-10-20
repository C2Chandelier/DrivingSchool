from django.urls import path
from . import views

app_name = 'Secretary'
urlpatterns =[
	path('',views.homeSecretary, name='homeSecretary'),
    path("student/<int:pk>/acount", views.studentDetail, name="studentDetail"),
    path('student/<int:pk>/planning', views.planningStudent, name='planningStudent'),
    path('studentList/', views.studentList, name='studentList'), 
    path('student/addStudent', views.addStudent, name='addStudent'),
    path('student/<int:pk>/delete', views.deleteStudent, name='deleteStudent'),
    path('confirmStudent/<int:pk>/to-delete', views.confirmDeleteStudent, name='confirmDeleteStudent'),
    path('student/<int:pk>/edit', views.editStudent, name='editStudent'),
    path('student/<int:pk>/addPlanning', views.addPlanning, name='addPlanning'),
    path('instructor/<int:pk>/account', views.instructorDetail, name='instructorDetail'),
    path('instructorList/', views.instructorList, name='instructorList'),
    path('instructor/<int:pk>/planning', views.planningInstructor, name='planningInstructor'),
    path('instructor/addInstructor', views.addInstructor, name='addInstructor'),
<<<<<<< HEAD
=======
    path('instructor/<int:pk>/addPlanning', views.addPlanningInstructor, name='addPlanningInstructor'),
    path('instructor/<int:pk>/delete', views.deleteInstructor, name='deleteInstructor'),
    path('confirmInsctructor/<int:pk>/to-delete', views.confirmDeleteInstructor, name='confirmDeleteInstructor'),
    path('instructor/<int:pk>/edit', views.editInstructor, name='editInstructor'),
>>>>>>> 5e3437d6f5988e267abd6946bc92533fdeed66d9
]

