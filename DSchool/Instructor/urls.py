from django.urls import path
from . import views

app_name = 'Instructor'
urlpatterns =[
	path('homeInstructor/',views.homeInstructor, name='homeInstructor'),
    path('', views.loginInstructor, name='loginInstructor'),
    path('profileStudent/<int:student_id>/', views.profileStudent, name='studentProfile'),
    path('detailInstructor', views.detailInstructor, name='detailInstructor'),
    path('addPlanningInstructor/', views.addPlanningInstructor, name='addPlanningInstructor'),
]