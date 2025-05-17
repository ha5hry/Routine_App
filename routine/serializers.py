from rest_framework import serializers
from . import models
import random, string
class RoutineSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Routine
        fields = ['title', 'description']

    def create(self, validated_data):
         request = self.context.get('request')
         random_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))
         validated_data['author'] = request.user
         validated_data['routine_id'] = 'routineid_' + random_id
         return super().create(validated_data)
    