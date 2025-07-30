from django.urls import re_path
from . import consumers
websocket_urlpatterns = [
    re_path(r"ws/routine/(?P<routine_slug>\w+)/$", consumers.RoutineConsumer.as_asgi()),
]