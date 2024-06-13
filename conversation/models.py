from django.db import models
from users.models import Users
from django.utils import timezone
# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    contact_user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='participant_contacts')
    main_user = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='owner_contacts')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return f"{self.main_user.username}'s contact {self.contact_user.username} | {self.name}"


class Messages(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    sent_time = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    receiver = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f"sender: {self.sender.username} | receiver: {self.receiver.username}"