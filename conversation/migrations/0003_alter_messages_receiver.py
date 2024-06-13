# Generated by Django 5.0.4 on 2024-06-13 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='received_messages', to='conversation.contacts'),
        ),
    ]
