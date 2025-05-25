from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name = 'register_user'),
    path('gender/choice/', views.GenderApiView.as_view(), name = 'gender_choice'),
    path('skill/', views.SkillApiView.as_view(), name='skill'),
    path('profile/<str:username>/', views.ProfileApiView.as_view(), name = 'profile'),
    path('edit/profile/', views.EditProfileApiView.as_view(), name = 'edit-profile'),
    path('profile/<str:username>/follow/', views.FollowApiView.as_view(), name='follow'),
]
