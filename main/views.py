from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson, Link
# Create your views here.

def index(request):
	context = {'lessons' : Lesson.objects.filter(show=True).order_by('week'), 
			   'links' : Link.objects.all().order_by('order')}
	def week_to_str(week):
		if week==0:
			return 'Poniedziałek'
		elif week==1:
			return 'Wtorek'
		elif week==2:
			return 'Środa'
		elif week==3:
			return 'Czwartek'
		elif week==4:
			return 'Piątek'
		elif week==5:
			return 'Sobota'
		elif week==6:
			return 'Niedziela'	
 
	for i in context['lessons']:
		if len(i.tags) > 0:
			i.tags = i.tags.split(";;")
	return render(request, 'index.html', context)