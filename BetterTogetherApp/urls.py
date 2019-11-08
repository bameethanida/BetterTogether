from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'BetterTogetherApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('shareride/', views.share_ride_index, name='share_ride_index1'),
    path('shareride/create', views.create_share_ride, name='create_share_ride')
]
