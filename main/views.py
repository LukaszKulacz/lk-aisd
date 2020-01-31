from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Classes, Lesson, Link, About
# Create your views here.

def index(request):
	context = {'classes':Classes.objects.filter(show=True)}
	return render(request, 'index.html', context)

def classes(request, id):
	entry = Classes.objects.filter(url=id, show=True)
	if entry.count() > 0:
		entry = entry.first()
		context = {'lessons' : Lesson.objects.filter(show=True, classes=entry).order_by('week'), 
			   'links' : Link.objects.filter(classes=entry).order_by('order'),
			   'about' : About.objects.first()}		

		for i in context['lessons']:
			if len(i.tags) > 0:
				i.tags = i.tags.split(";;")
		return render(request, 'classes.html', context)
	else:
		return redirect('/')