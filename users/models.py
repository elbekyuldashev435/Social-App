from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True, default='default_user/user_img.png')
    bio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username