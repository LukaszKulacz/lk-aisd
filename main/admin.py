from django.contrib import admin
from django.contrib.sites.models import Site
from preferences.admin import PreferencesAdmin
from .models import Lesson, Link, MyPreferences
# Register your models here.

admin.site.register(MyPreferences, PreferencesAdmin)   

class LessonAdmin(admin.ModelAdmin):
	list_display = ('week', 'show', 'name')
admin.site.register(Lesson, LessonAdmin)

class LinkAdmin(admin.ModelAdmin):
	list_display = ('order', 'name')
admin.site.register(Link, LinkAdmin)
