# Generated by Django 5.1 on 2024-09-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default="didn't set", max_length=250),
            preserve_default=False,
        ),
    ]
