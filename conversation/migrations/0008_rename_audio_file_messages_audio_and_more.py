# Generated by Django 5.0.4 on 2024-06-14 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0007_remove_messages_message_remove_messages_message_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='audio_file',
            new_name='audio',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='docs_file',
            new_name='docs',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='picture_file',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='video_file',
            new_name='video',
        ),
    ]
