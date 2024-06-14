from django.db import models
from users. models import Users
# Create your models here.


class Topics(models.Model):
    topic_name = models.CharField(max_length=150)

    class Meta:
        db_table = 'topics'

    def __str__(self):
        return self.topic_name


class Posts(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='posts/images', blank=True, null=True)
    post_video = models.ImageField(upload_to='posts/videos', blank=True, null=True)
    post_description = models.TextField()

    class Meta:
        db_table = 'posts'