# Generated by Django 5.1 on 2024-08-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='star_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(null=True),
        ),
    ]
