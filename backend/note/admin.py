from django.contrib import admin
from .models import Note, Tag, NotebookColumn, UserFavoriteNote
# Register your models here.

class NoteAdmin(admin.ModelAdmin):  
    list_display = ['id', 'title'] 

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tagname']

class NotebookColumnAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title']

class UserFavoriteNoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'note']

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(NotebookColumn, NotebookColumnAdmin)
admin.site.register(UserFavoriteNote, UserFavoriteNoteAdmin)