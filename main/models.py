from django.db import models
from preferences.models import Preferences
import datetime, django

# Create your models here.
class MyPreferences(Preferences):
	class Meta:
		verbose_name = "My preferences"
		verbose_name_plural = "My preferences"
	__module__ = 'preferences.models'

	title = models.CharField(max_length=255, default='Title')
	email = models.CharField(max_length=255, default='mail@mail.com')
	name = models.CharField(max_length=255, default='Name')
	DAYS = [('Poniedziałek','Poniedziałek'),
		 	('Wtorek','Wtorek'),
		 	('Środa','Środa'),
		 	('Czwartek','Czwartek'),
		 	('Piątek','Piątek'),
		 	('Sobota','Sobota'),
		 	('Niedziela','Niedziela'),]
	day = models.CharField(max_length=255, default=DAYS[0][0],choices=DAYS)
	time_from = models.TimeField(default=django.utils.timezone.now)
	time_to = models.TimeField(default=django.utils.timezone.now)
	

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
	