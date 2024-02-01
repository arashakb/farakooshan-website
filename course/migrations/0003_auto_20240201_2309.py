# Generated by Django 3.2.23 on 2024-02-01 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20231219_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='course/default.jpg', upload_to='course/'),
        ),
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(null=True, upload_to='course/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
