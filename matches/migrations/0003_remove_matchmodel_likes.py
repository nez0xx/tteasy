# Generated by Django 3.2.9 on 2022-04-19 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_matchmodel_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchmodel',
            name='likes',
        ),
    ]
