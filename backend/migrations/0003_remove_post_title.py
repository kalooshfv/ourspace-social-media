# Generated by Django 4.1 on 2023-02-24 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
