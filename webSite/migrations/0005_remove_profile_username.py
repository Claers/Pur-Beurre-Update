# Generated by Django 2.1.4 on 2019-02-05 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0004_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
