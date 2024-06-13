from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    bio = models.TextField()

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username
