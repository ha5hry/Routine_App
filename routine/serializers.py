from rest_framework import serializers
from . import models
import random, string
class RoutineSerializer(serializers.ModelSerializer):
    routine_slug = serializers.SerializerMethodField(read_only = True)
    def get_routine_slug(self, obj):
         return obj.slug
    class Meta:
        model = models.Routine
        fields = ['title', 'description', 'routine_slug']

    def create(self, validated_data):
         request = self.context.get('request')
         random_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
         validated_data['author'] = request.user
         validated_data['routine_id'] =  random_id
         return super().create(validated_data)
    
class TodoSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')
    task_author = serializers.SerializerMethodField(read_only = True)
    task_title = serializers.SerializerMethodField (read_only = True)


    def get_task_author(self, obj):
        return obj.details.author.email
    def get_task_title(self, obj):
        return obj.details.title

    class Meta:
        model = models.Todo
        fields = ['task_title', 'task_author', 'activity_name', 'start_time', 'end_time']
    
    def create(self, validated_data):
        request = self.context.get('request')
        routine_slug = self.context.get('routine_slug')
        get_routine = models.Routine.objects.get(slug =  routine_slug)
        validated_data['details'] = get_routine
        return super().create(validated_data)