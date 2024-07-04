from django.contrib import admin
from .models import Note, Tag
# Register your models here.

class NoteAdmin(admin.ModelAdmin):  
    list_display = ['id', 'title'] 

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tagname']

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)