from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name = 'register_user'),
    path('profile/<str:username>/', views.ProfileApiView.as_view(), name = 'profile'),
    path('skill/', views.SkillApiView.as_view(), name='skill'),
    path('follow/', views.FollowApiView.as_view(), name='follow'),
    path('unfollow/', views.FollowApiView.as_view(), name='unfollow'),
]
