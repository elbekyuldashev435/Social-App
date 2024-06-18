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

    def __str__(self):
        return f"author: {self.user.username} | title: {self.post_title}"


class Share(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender_user')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='receiver_user')
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'share'

    def __str__(self):
        return f"sender: {self.sender.username} --> receiver: {self.receiver.username}"


class Save(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    saved_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'save'

    def __str__(self):
        return f"user: {self.user.username} --> post: {self.post.post_title}"