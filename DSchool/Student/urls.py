from django.urls import path
from . import views

app_name = 'Student'
urlpatterns =[
	path('homeStudent/',views.homeStudent, name='homeStudent'),
    path('', views.loginStudent, name='loginStudent'),
    path('detailStudent/<int:student_id>/',views.detailStudent, name='detailStudent'),
]

