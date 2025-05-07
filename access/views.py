from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Skill, Follow
from .serializers import RegisterSerializer, SkillSerializer, ProfileSerializer, FollowSerializer
# Create your views here.
class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(APIView):

    def get(self, request, username):
        instance = Profile.objects.get(username = username)
        follow_instance, created = Follow.objects.get_or_create(profile = request.user)
        serializer = ProfileSerializer(instance)
        return Response(serializer.data)
class SkillApiView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
class FollowApiView(APIView):
    def post(self, request):
        

        # serializer = FollowSerializer( context = {'request':request})
        # serializer.save()
        return Response('let seee')
        
    def get(self, request):
        instance = Follow.objects.all()
        serializer = FollowSerializer(instance, many = True)
        return Response(serializer.data)
#     def post(self, request):
#         user = request.user
        
#         if request.data.get('follow') == 'follow':
