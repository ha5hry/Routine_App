from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name = 'register_user'),
    path('skill/', views.SkillApiView.as_view(), name='skill'),
    path('profile/<str:username>/', views.ProfileApiView.as_view(), name = 'profile'),
    path('profile/<str:username>/follow/', views.FollowApiView.as_view(), name='follow'),
    path('unfollow/', views.FollowApiView.as_view(), name='unfollow'),
]
