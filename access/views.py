from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Skill, Follow
from .serializers import RegisterSerializer, SkillSerializer, ProfileSerializer, FollowSerializer
from common import permissions

# Create your views here.
class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data, context = {'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SkillApiView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
    
class ProfileApiView(APIView):
    permission_classes =[permissions.AccessPermission]
    def get(self, request, username):
        instance = Profile.objects.get(username = username)
        no_of_following= Follow.objects.filter(user_following = request.user).count()
        no_of_followers = Follow.objects.filter(user_followed = request.user).count()
        serializer = ProfileSerializer(instance)
        return Response({'profile_data':serializer.data, 'following_data': no_of_following, 'followers_data': no_of_followers})

class EditProfileApiView(APIView):
    permission_classes = [permissions.AccessPermission]
    def put(self, request):
        instance = Profile.objects.get(username = request.user.username)
        serializer = ProfileSerializer(instance, request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
        return Response ('Profile updated', status= status.HTTP_202_ACCEPTED)
    def patch(self, request):
        instance = Profile.objects.get(username = request.user.username)
        serializer = ProfileSerializer(instance, request.data, context = {'request':request}, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response ('Profile updated', status= status.HTTP_202_ACCEPTED)
        return Response (serializer.errors)
class FollowApiView(APIView):
    permission_classes =[permissions.AccessPermission]
    def post(self, request, username):
        # This IF bock checks for the keyword 'follow' is having the word 'follow' passed in the request data to the endpoint
        if request.data.get('follow') == 'follow':
            # all_user_following is to get all the Follow model object of where their user_following fields is the object of the current logged-in user
            all_user_following = Follow.objects.filter(user_following = request.user)
            count_f = Follow.objects.filter(user_following = request.user).count()
            print("this is the following count" ,count_f)
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
            return Response('hola', status=status.HTTP_201_CREATED)
        # This IF bock checks for the keyword 'follow' is having the word 'unfollow' passed in the request data to the endpoint
        elif request.data.get('follow') == 'unfollow':
            # user_followed this get the user being followed by the logged-in user through the username in the URL to get the profile object fro the Profile Model
            user_followed = Profile.objects.get(username = username)
            # assign the profile being followed to the 'user_followed' field in the Follow object
            instance = Follow.objects.get(user_following = request.user, user_followed = user_followed)
            instance.delete()
            return Response('Deleted')
        
    def get(self, request, username):
        following_count = Follow.objects.filter(user_following = request.user).count()
        followers_count = Follow.objects.filter(user_followed = request.user).count()
        print(following_count, followers_count)
        instance = Follow.objects.all()
        serializer = FollowSerializer(instance, many = True, context = {'request': request})
        return Response(serializer.data)

