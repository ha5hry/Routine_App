from django.db import models
from access.models import Profile
from django.utils.text import slugify
# Create your models here.

class Routine(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='routine')
    routine_id = models.CharField(max_length=23, unique=True, blank=False)
    title =  models.CharField(max_length = 50)
    description = models.TextField()
    slug = models.SlugField(unique=True, null= True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, self.id)
            return super().save()
class Todo(models.Model):
    details = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_details')
    activity_name = models.CharField(max_length = 100)
    start_time = models.TimeField()
    end_time = models.TimeField()