# Generated by Django 3.2.23 on 2024-02-07 09:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, default='Default Content', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='Default Content', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(default='Post Title', max_length=255, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fa',
            field=models.CharField(default='Post Title', max_length=255, verbose_name='title'),
        ),
    ]
