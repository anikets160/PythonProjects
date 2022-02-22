from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('home', views.home, name ='home'),
    path('', views.login, name ='login'),
    path('signup', views.signup, name ="signup"),
    path('signin', views.signin, name ="signin"),
    path('signout', views.signout, name ="signout"),
]