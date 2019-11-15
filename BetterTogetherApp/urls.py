from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'BetterTogetherApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('shareride/', views.share_ride_index, name='share_ride_index1'),
    path('shareride/create', views.create_share_ride, name='create_share_ride'),
    path('shareride/remove/<int:shareride_id>', views.delete_share_ride, name='delete_share_ride'),
    path('sharepromo/', views.share_promotion_index, name='share_promotion_index1'),
    path('sharepromo/create', views.create_share_promotion, name='create_share_promotion'),
    path('sharepromo/remove/<int:sharepromo_id>', views.delete_share_promotion, name='delete_share_promotion')
]
