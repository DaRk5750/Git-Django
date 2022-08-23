from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('newregister', views.newregister, name='newregister'),
    path('login', views.login, name='login'),
    path('loginuser', views.loginuser, name='loginuser'),
]