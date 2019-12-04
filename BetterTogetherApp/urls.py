from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'BetterTogetherApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('shareride/', views.share_ride_index, name='share_ride_index1'),
    path('shareride/create', views.create_share_ride, name='create_share_ride'),
    path('shareride/remove/<int:shareride_id>', views.delete_share_ride, name='delete_share_ride'),
    path('shareride/join/<int:shareride_id>', views.join_share_ride, name='join_share_ride'),
    path('sharepromo/', views.share_promotion_index, name='share_promotion_index1'),
    path('sharepromo/create', views.create_share_promotion, name='create_share_promotion'),
    path('sharepromo/remove/<int:sharepromo_id>', views.delete_share_promotion, name='delete_share_promotion'),
    path('sharepromo/join/<int:sharepromo_id>', views.join_share_promotion, name='join_share_promotion'),
    path('sharefood/', views.share_food_index, name='share_food_index1'),
    path('sharefood/create', views.create_share_food, name='create_share_food'),
    path('sharefood/remove/<int:sharefood_id>', views.delete_share_food, name='delete_share_food'),
    path('sharefood/join/<int:sharefood_id>', views.join_share_food, name='join_share_food'),
    path('', include('social_django.urls', namespace="oauth"))
]
