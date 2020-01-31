from django.db import models
from single_instance_model.models import SingleInstanceModel
import datetime, django

# Create your models here.
class About(models.Model, SingleInstanceModel):
	title = models.CharField(max_length=255, default='Default Title')
	email = models.CharField(max_length=255, default='mail@mail.com')
	name = models.CharField(max_length=255, default='Default Name')
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

class Classes(models.Model):
	def __str__(self):
		return self.name
	url = models.CharField(max_length=255, default='Example', unique=True)
	name = models.CharField(max_length=255, default='Example classes name', unique=True)
	description = models.TextField(default='Example classes description', blank=True)
	show = models.BooleanField(default=True)

class Lesson(models.Model):
	classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
	week = models.IntegerField(unique=True, default=1)
	name = models.CharField(max_length=255, default='')
	tags = models.CharField(max_length=255, default='', blank=True)
	description = models.TextField(default='')
	show = models.BooleanField(default=True)

class Link(models.Model):
	classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
	order = models.IntegerField(unique=True, default=1)
	name = models.CharField(max_length=255, default='')
	link = models.URLField(default='https://')
	description = models.TextField(default='')
	