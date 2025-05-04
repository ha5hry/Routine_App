from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

# Create your models here.
class Profile(AbstractUser):
    username = models.CharField(unique=True)
    email = models.EmailField(_("Email Address"), unique=True)
    bio = models.TextField(_("Bio"), max_length=250, blank = True)
    birthday=models.DateField(_("Birthday"), blank= True, null=True)
    pfp = models.FileField(upload_to="",null=True, blank=True )
    gender_choice = (('m', 'Male'),
                      ('f', 'Female'),)
    gender = models.CharField(_("Gender"), max_length=1, choices=gender_choice)
    phone_number = models.CharField(_("Phone Number"), max_length=15, unique=True, blank=True, null= True )
    date_joined = models.DateField(_("Date Joined"), auto_now_add=True)


    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

class Skill(models.Model):
    skill_choice = (
        ('product_manager', 'ProductManager'),('data_analytics', 'Data Analytics'),('frontend_development', 'Frontend Development'), 
        ('backend_development', 'Backend Development'), ('uiux design', 'UI/UX Design'), ('blockchain_development', 'Blockchain Development'),
        ('technical_writing', 'Technical Writing'), ('game_development', 'Game Development')
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'profile_skill')
    skill = models.CharField(_('Skills'),max_length=50, choices= skill_choice)