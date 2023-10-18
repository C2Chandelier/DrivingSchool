from django.urls import path
from . import views

app_name = 'Student'
urlpatterns =[
	path('homeStudent/',views.homeStudent, name='planning-list'),
    path('', views.loginStudent, name='loginStudent'),



    path('students/', views.student, name='student-list'), 
    path("students/<int:pk>/acount", views.StudentView.as_view(), name="student-detail"),
    path('students/<int:pk>/planning', views.PlanningView.as_view(), name='planning-list'),
    path('planning', views.planning, name='planning-list'),

]