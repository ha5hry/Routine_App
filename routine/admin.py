from django.contrib import admin
from .models import Routine, Todo

# Register your models here.

class RoutineAdmin(admin.ModelAdmin):
    list_display = ['get_author','title', 'slug']

    def get_author(self, obj):
        return obj.author

admin.site.register(Routine, RoutineAdmin)

admin.site.register(Todo)