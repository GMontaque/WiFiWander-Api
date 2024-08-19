# Generated by Django 5.1 on 2024-08-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifi_locations', '0004_remove_wifilocation_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wifilocation',
            name='image',
            field=models.ImageField(default='../default_profile_q35ywj', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='wifilocation',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
