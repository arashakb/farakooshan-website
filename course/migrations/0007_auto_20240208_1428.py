# Generated by Django 3.2.23 on 2024-02-08 10:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_course_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
        migrations.RemoveField(
            model_name='course',
            name='cpdunit',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='location',
        ),
        migrations.RemoveField(
            model_name='course',
            name='objectives',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
        migrations.RemoveField(
            model_name='course',
            name='whoshouldattend',
        ),
        migrations.AddField(
            model_name='category',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='category',
            name='content_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default='0', max_length=255, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fa',
            field=models.CharField(default='0', max_length=255, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='course',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='course',
            name='content_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='course',
            name='cpdunit_en',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='cpdunit'),
        ),
        migrations.AddField(
            model_name='course',
            name='cpdunit_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='cpdunit'),
        ),
        migrations.AddField(
            model_name='course',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='course',
            name='description_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='course',
            name='location_en',
            field=models.CharField(default='dafault string', max_length=255, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='course',
            name='location_fa',
            field=models.CharField(default='dafault string', max_length=255, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='course',
            name='objectives_en',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='objectives'),
        ),
        migrations.AddField(
            model_name='course',
            name='objectives_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='objectives'),
        ),
        migrations.AddField(
            model_name='course',
            name='price_en',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='course',
            name='price_fa',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(default='dafault string', max_length=255, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_fa',
            field=models.CharField(default='dafault string', max_length=255, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='course',
            name='whoshouldattend_en',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='whoshouldattend'),
        ),
        migrations.AddField(
            model_name='course',
            name='whoshouldattend_fa',
            field=ckeditor.fields.RichTextField(blank=True, default='dafault string', null=True, verbose_name='whoshouldattend'),
        ),
    ]
