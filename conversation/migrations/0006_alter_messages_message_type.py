# Generated by Django 5.0.4 on 2024-06-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0005_remove_messages_audio_remove_messages_docs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message_type',
            field=models.CharField(choices=[('audio', 'audio'), ('video', 'video'), ('picture', 'picture'), ('docs', 'docs')], max_length=10),
        ),
    ]
