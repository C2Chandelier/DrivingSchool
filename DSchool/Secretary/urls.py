from django.urls import path
from . import views

app_name = 'Secretary'
urlpatterns =[
	path('',views.homeSecretary, name='homeSecretary'),
]