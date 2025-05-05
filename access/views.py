from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Skill, Follow
from .serializers import RegisterSerializer
# Create your views here.
class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)