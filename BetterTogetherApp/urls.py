from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'BetterTogetherApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.signup_login, name='login'),
    path('home/',views.index, name='home'),
]
