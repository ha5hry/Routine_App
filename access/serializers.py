from rest_framework import serializers, response
from .models import Profile, Skill, Follow

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True)
    class Meta:
        model = Profile
        exclude = ('date_joined',)
        extra_kwargs = {'password':{'write_only': True}}
       

    def validate(self, data):
            if data['password2'] != data['password']:
                raise ValueError("Your password does not match")
            return data
        
    def create(self, validated_data):
            validated_data.pop('password2')
            user = Profile.objects.create_user(**validated_data)
            return user

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
          model = Profile
          fields = ['pfp', 'username', 'full_name', 'email', 'phone_number' , 'bio','birthday', 'gender',  ]
          extra_kwargs = {'password':{'write_only':True }}


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['skill']

    def create(self, validated_data):
         request = self.context.get('request')
         validated_data['profile'] = request.user
         return super().create(validated_data)
    
class FollowSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only = True)
    following_count = serializers.SerializerMethodField(read_only = True)
    followers_count = serializers.SerializerMethodField(read_only = True)
    def get_username(self, obj):
         return obj.user_following.username 
    
    def get_following_count( self, obj):
        request = self.context.get('request')
        return Follow.objects.filter(user_following = request.user).count()
    
    def get_followers_count(self, obj):
        request = self.context.get('request')
        return Follow.objects.filter(user_followed = request.user).count()
    class Meta:
          model = Follow
          fields = [ 'username', 'following_count', 'followers_count', 'user_following', 'user_followed'] 



    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     validated_data['profile'] = request.user
    #     return super().create(validated_data)