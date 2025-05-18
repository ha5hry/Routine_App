from django.urls import path
from . import views

urlpatterns = [
    path('routine/title/', views.RoutineTitleApiView.as_view(), name = 'routine_title'),
    path('create/routine/<slug:routine_slug>/', views.CreateRoutineAPIView.as_view(), name = 'routine'),
]
