from django.contrib import admin
from .models import Lesson, Link, Settings
# Register your models here.
    
class LessonAdmin(admin.ModelAdmin):
	list_display = ('week', 'show', 'name')

admin.site.register(Lesson, LessonAdmin)

class LinkAdmin(admin.ModelAdmin):
	list_display = ('order', 'name')

admin.site.register(Link, LinkAdmin)

class SettingsAdmin(admin.ModelAdmin):
	list_display = ('title', 'name', 'email')

	def has_add_permission(self, request):
		num_objects = self.model.objects.count()
		return num_objects == 0

admin.site.register(Settings, SettingsAdmin)