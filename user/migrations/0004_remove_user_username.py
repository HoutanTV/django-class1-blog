# Generated by Django 5.1 on 2024-09-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
