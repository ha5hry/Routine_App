from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Skill, Follow

# Register your models here.
class ProfileUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "username", "bio", "birthday", "pfp", "gender", "phone_number", )}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", )}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username","email", "password1", "password2", "phone_number"),
        }),
    )
    readonly_fields = ('date_joined',)
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

admin.site.register(Profile, ProfileUserAdmin)
admin.site.register(Skill)

# class FollowAdmin(admin.ModelAdmin):
#     list_display = ['username', 'follower', 'following']
# admin.site.register(Follow, FollowAdmin)