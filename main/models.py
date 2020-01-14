from django.db import models
import datetime, django

# Create your models here.
class Lesson(models.Model):
	week = models.IntegerField(unique=True, default=1)
	name = models.CharField(max_length=255, default='')
	tags = models.CharField(max_length=255, default='', blank=True)
	description = models.TextField(default='')
	show = models.BooleanField(default=True)

class Link(models.Model):
	order = models.IntegerField(unique=True, default=1)
	name = models.CharField(max_length=255, default='')
	link = models.URLField(default='https://')
	description = models.TextField(default='')

class Settings(models.Model):
	title = models.CharField(max_length=255, default='')
	email = models.CharField(max_length=255, default='')
	date = models.DateField(default=django.utils.timezone.now)
	time_from = models.TimeField(default=django.utils.timezone.now)
	time_to = models.TimeField(default=django.utils.timezone.now)
	name = models.CharField(max_length=255, default='')

	