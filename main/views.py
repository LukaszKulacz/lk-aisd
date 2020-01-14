from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson, Link
# Create your views here.
def index(request):
	context = {'lessons' : Lesson.objects.filter(show=True).order_by('week'), 
			   'links' : Link.objects.all().order_by('order')}
	for i in context['lessons']:
		if len(i.tags) > 0:
			i.tags = i.tags.split(";;")
	return render(request, 'index.html', context)