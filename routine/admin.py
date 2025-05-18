from django.contrib import admin
from .models import Routine, Todo

# Register your models here.

class RoutineAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']

admin.site.register(Routine, RoutineAdmin)

admin.site.register(Todo)