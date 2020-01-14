# Generated by Django 3.0.2 on 2020-01-14 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=1, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('tags', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('show', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('link', models.URLField(default='https://')),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time_from', models.TimeField(default=django.utils.timezone.now)),
                ('time_to', models.TimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
