from django.db import models
from access.models import Profile
# Create your models here.

class Routine(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='routine')
    routine_id = models.CharField(max_length=23, unique=True, blank=False)
    title =  models.CharField(max_length = 50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

class Todo(models.Model):
    details = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_details')
    activity_name = models.CharField(max_length = 100)
    start_time = models.TimeField()
    end_time = models.TimeField()