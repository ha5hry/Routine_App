from rest_framework.serializers import ModelSerializer
from .models import Profile

class RegisterSerializer(ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('date_joined')
        