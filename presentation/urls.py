from django.shortcuts import render
from django.urls import path

from . import views


app_name = 'presentation'
urlpatterns = [
	 # ex: /presentation/
    path('', views.index, name='index'),

]