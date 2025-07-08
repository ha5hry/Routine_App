from rest_framework.permissions import BasePermission
from access.models import Profile, Follow, Skill


class AccessPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
