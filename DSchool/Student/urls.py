from django.urls import path
from . import views

app_name = 'Student'
urlpatterns =[
	path('homeStudent/',views.homeStudent, name='homeStudent'),
    path('', views.loginStudent, name='loginStudent'),
    path('detailStudent/',views.detailStudent, name='detailStudent'),
]

