from django.urls import path
from . import api_views, views

urlpatterns = [
    path("", views.LandingPageView.as_view(), name="landing-page"),
    path("api/register/", api_views.RegisterApiView.as_view(), name="registration_api"),
    path("api/log-in/", api_views.LoginApiView.as_view(), name="login_api"),
    path("api/skill/", api_views.SkillApiView.as_view(), name="skill_api"),
    path("api/profile/<str:username>/", api_views.ProfileApiView.as_view(), name="profile_api"),
    path("api/edit/profile/", api_views.EditProfileApiView.as_view(), name="edit-profile_api"),
    path("api/profile/<str:username>/follow/",api_views.FollowApiView.as_view(),name="follow_api",),
]
