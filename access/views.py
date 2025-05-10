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


class MyProfileApiView(APIView):
    def get(self, request):
        # user_following = Profile.objects.get(profile = request.user)
        instance, created = Follow.objects.get_or_create(profile = request.user)
        serializer = FollowSerializer(instance)
        return Response(serializer.data)

class FollowApiView(APIView):
    def post(self, request, username):
        if request.data.get('follow') == 'follow':
            #user_following is to get or create the Follow object for the logged in user 
            user_following = Follow.objects.get(profile = request.user)
            # profile_user is to get the th objects in the access.profile model of the username passed in the URL
            profile_user = Profile.objects.get(username = username)
            # profile_followers either fetches or create a new object of Follow model for the username object
            profile_followers, created = Follow.objects.get_or_create(profile = profile_user)
            print(f' Old {user_following.following, profile_followers.follower}')
            user_following.following += 1
            profile_followers.follower += 1
            user_following.save()
            profile_followers.save()
            print(f'New {user_following.following, profile_followers.follower}')
            serializer = FollowSerializer(request.data)
            return Response(serializer.data)
        
    def get(self, request, username):

        # user_following, created = Follow.objects.get_or_create(profile = request.user)
        # profile_user = Profile.objects.get(username = username)
        # profile_followers, created = Follow.objects.get_or_create(profile = profile_user)
        # print(f'{user_following.following, profile_followers.follower}')
        # user_following.following + 2
        # profile_followers.follower +2

        
        # user_following.save()
        # profile_followers.save()
        # print (f'user_following {user_following.following, profile_followers.follower}')
        instance = Follow.objects.all()
        serializer = FollowSerializer(instance, many = True)
        return Response(serializer.data)
        # elif request.data.get('follow') == 'unfollow':
        #     instance = Follow.objects.get(profile = request.user)
        #     instance.following =- 1
        #     instance.save()

#     def post(self, request):
#         user = request.user
        
#         if request.data.get('follow') == 'follow':
