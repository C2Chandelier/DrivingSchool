from django.urls import path
from . import views

app_name = "DSchool"

urlpatterns = [
    path('students/', views.student, name='student-list'), 
    path("students/<int:pk>/acount", views.student_detail_view, name="student-detail"),
    path('students/<int:pk>/planning', views.planning_view, name='planning-list'),
    path('planning', views.planning, name='planning-list-all'),

    path('students/add-member', views.student_form, name='student_form'),
    path('students/<int:pk>/delete', views.delete_student, name='delete-student'),
    path('students/<int:pk>/to-delete', views.student_to_delete, name='student-to-delete'),
    path('students/<int:pk>/edit', views.edit_student, name='student-to-edit'),

    path('students/<int:pk>/add-rdv', views.add_rdv, name='add-rdv'),



    


]

