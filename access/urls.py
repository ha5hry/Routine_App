from django.urls import path
from . import api_views

urlpatterns = [
    path("register/", api_views.RegisterApiView.as_view(), name="registration_api"),
    path("log-in/", api_views.LoginApiView.as_view(), name="login_api"),
    path("skill/", api_views.SkillApiView.as_view(), name="skill_api"),
    path("profile/<str:username>/", api_views.ProfileApiView.as_view(), name="profile_api"),
    path("edit/profile/", api_views.EditProfileApiView.as_view(), name="edit-profile_api"),
    path("profile/<str:username>/follow/",api_views.FollowApiView.as_view(),name="follow_api",),
]
