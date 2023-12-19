# Generated by Django 3.2.23 on 2023-12-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('description', models.TextField()),
                ('objectives', models.TextField()),
                ('whoshouldattend', models.TextField()),
                ('cpdunit', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
