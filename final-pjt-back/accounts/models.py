from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name = 'followers')
    introduce = models.CharField(max_length=255)
    profileimg = models.ImageField(null=True)
    nickname = models.CharField(max_length=20)