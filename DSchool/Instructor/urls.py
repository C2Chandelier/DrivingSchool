from django.urls import path
from . import views

app_name = 'Instructor'
urlpatterns =[
	path('homeInstructor/',views.homeInstructor, name='homeInstructor'),
    path('', views.loginInstructor, name='loginInstructor'),
    path('profileStudent/<int:student_id>/', views.profileStudent, name='studentProfile'),
    path('detailInstructor', views.detailInstructor, name='detailInstructor'),
    path('addPlanningInstructor/', views.addPlanningInstructor, name='addPlanningInstructor'),

    path('supprimer_planning/<int:planning_id>/', views.supprimer_planning, name='supprimer_planning'),
    path('confirmation_suppression/<int:planning_id>/', views.confirmer_suppression, name='confirmer_suppression'),
    path('instructor/planning/<int:planning_id>/modifier/', views.modifier_entry, name='modifier_entry'),
]