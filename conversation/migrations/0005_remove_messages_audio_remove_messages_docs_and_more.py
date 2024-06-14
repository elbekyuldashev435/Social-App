# Generated by Django 5.0.4 on 2024-06-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0004_messages_audio_messages_docs_messages_picture_and_more'),
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
            name='message_type',
            field=models.CharField(choices=[('audio', 'audio'), ('video', 'video'), ('picture', 'picture'), ('docs', 'docs')], default='picture', max_length=10),
        ),
    ]
