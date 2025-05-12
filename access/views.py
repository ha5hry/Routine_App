from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Skill, Follow
from .serializers import RegisterSerializer, SkillSerializer, ProfileSerializer, FollowSerializer

# Create your views here.
class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data, context = {'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(APIView):

    def get(self, request, username):
        instance = Profile.objects.get(username = username)
        user_follow_obj, created = Follow.objects.get_or_create(profile = request.user)
        serializer = ProfileSerializer(instance)
        return Response(serializer.data)
class SkillApiView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)


class MyProfileApiView(APIView):
    def get(self, request):
        # user_following = Profile.objects.get(profile = request.user)
        instance, created = Follow.objects.get_or_create(profile = request.user)
        serializer = FollowSerializer(instance)
        return Response(serializer.data)

class FollowApiView(APIView):
    def post(self, request, username):
        # all_user_following is to get all the Follow model object of where their user_following fields is the object of the current logged-in user
        all_user_following = Follow.objects.filter(user_following = request.user)
        # get_user_followed is to get the user being followed in the profile model 
        get_user_followed = Profile.objects.get(username = username)
        # this FOR block is to loop on each objects from the 'all_user_following' model 
        for each_user_following in all_user_following:
            # Thus IF block is to check if the current logged-in user hasn't followed the profile about to be followed, to avoid duplication
            if each_user_following.user_following == request.user and each_user_following.user_followed == get_user_followed:
                #If TRUE the it returns the Response below, but if FALSE it exit the block and continue with the remaining lines of code
                return Response("Profile has been followed by this user")
        # user_following is to create an object in Follow Model for the current logged-in User
        user_following = Follow.objects.create(user_following = request.user)
        # user_followed this get the user being followed by the logged-in user through the username in the URL to get the profile object fro the Profile Model
        user_followed = Profile.objects.get(username = username)

        # assign the profile being followed to the 'user_followed' field in the Follow object
        user_following.user_followed = user_followed

        user_following.save()

        return Response('Successful')
        
    def get(self, request, username):
        instance = Follow.objects.all()
        serializer = FollowSerializer(instance, many = True)
        return Response(serializer.data)

