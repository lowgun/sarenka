# Generated by Django 3.1.7 on 2021-06-08 21:29

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('engines', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='censyscredentials',
            managers=[
                ('credentials', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='shodancredentials',
            managers=[
                ('credentials', django.db.models.manager.Manager()),
            ],
        ),
    ]
