from rest_framework import serializers
from . import models
import random, string
class RoutineSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Routine
        fields = ['title', 'description']

    def create(self, validated_data):
         request = self.context.get('request')
         random_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
         validated_data['author'] = request.user
         validated_data['routine_id'] =  random_id
         return super().create(validated_data)
    
class TodoSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')


    class Meta:
        model = models.Todo
        fields = ['activity_name', 'start_time', 'end_time']
    
    def create(self, validated_data):
        request = self.context.get('request')
        routine_slug = self.context.get('routine_slug')
        get_routine = models.Routine.objects.get(slug =  routine_slug)
        validated_data['details'] = get_routine
        return super().create(validated_data)