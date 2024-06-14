# Generated by Django 5.0.4 on 2024-06-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0009_messages_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='docs',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='video',
        ),
        migrations.AddField(
            model_name='messages',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='messages/files/'),
        ),
    ]