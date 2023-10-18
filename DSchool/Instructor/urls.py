from django.urls import path
from . import views

app_name = 'Instructor'
urlpatterns =[
	path('homeInstructor/',views.homeInstructor, name='homeInstructor'),
    path('', views.loginInstructor, name='loginInstructor'),

    path("instructor/planning", views.planning, name="planning"),
    path('user/<int:pk>/', views.StudentProfileView.as_view(), name='student_profile'),
    path('instructor/<int:pk>/', views.InstructorProfileView.as_view(), name='instructor_profile'),
    path('new/', views.add_entry_planning, name='new_entry'),
]