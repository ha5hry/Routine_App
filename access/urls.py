from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name = 'register_user'),
    path('skill/', views.SkillApiView.as_view(), name='skill'),
]
