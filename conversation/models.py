from django.db import models
from users.models import Users
from django.utils import timezone
# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    contact_user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='contact_user_contacts')
    main_user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='main_user_contacts')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return f"{self.main_user.username}'s contact {self.contact_user.username} | {self.name}"


class Messages(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='sent_messages')
    message = models.TextField(null=True)
    picture = models.ImageField(upload_to='messages/picture/', blank=True, null=True)
    audio = models.FileField(upload_to='messages/audio/', blank=True, null=True)
    video = models.FileField(upload_to='messages/video/', blank=True, null=True)
    docs = models.FileField(upload_to='messages/docs/', blank=True, null=True)
    sent_time = models.DateTimeField(default=timezone.now)
    receiver = models.ForeignKey(Contacts, on_delete=models.DO_NOTHING, related_name='received_messages')

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f"sender: {self.sender.username} --> receiver: {self.receiver.contact_user.username}"