# Generated by Django 3.2.23 on 2024-02-08 10:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20240207_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_fa',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_fa',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]