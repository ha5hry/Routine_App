from django.urls import path
from . import views

urlpatterns = [
    path('create/routine/', views.RoutineApiView.as_view(), name = 'routine'),
]
