# Generated by Django 5.1 on 2024-08-18 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wifi_locations', '0003_wifilocation_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wifilocation',
            name='star_rating',
        ),
    ]
