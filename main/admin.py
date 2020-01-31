from django.contrib import admin
from .models import Classes, Lesson, Link, About
from single_instance_model.admin import SingleInstanceModelAdmin
# Register your models here.



class AboutAdmin(SingleInstanceModelAdmin):
	pass
admin.site.register(About, AboutAdmin)

class ClassesAdmin(admin.ModelAdmin):
	list_display = ('url', 'name', 'show',)
admin.site.register(Classes, ClassesAdmin)

class LessonAdmin(admin.ModelAdmin):
	list_display = ('name', 'week', 'show',)
	ordering = ('week',)
admin.site.register(Lesson, LessonAdmin)

class LinkAdmin(admin.ModelAdmin):
	list_display = ('order', 'name')
admin.site.register(Link, LinkAdmin)
