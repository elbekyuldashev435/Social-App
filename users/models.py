from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username


class ProfileImages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = "ProfileImages"

    def __str__(self):
        return self.user
