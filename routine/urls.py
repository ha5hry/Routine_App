from django.urls import path
from . import api_views, views

urlpatterns = [
    path('api/routine/title/', api_views.RoutineTitleApiView.as_view(), name = 'routine_title_api'),
    path('api/create/routine/add/<slug:routine_slug>/', api_views.RoutineTaskAPIView.as_view(), name = 'add_routine_api'),
    path('api/create/routine/', api_views.CreateRoutineAPIView.as_view(), name = 'create_routine_api'),
]