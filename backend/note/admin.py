from django.contrib import admin
from .models import Note, Tag, NotebookColumn, UserFavoriteNote
# Register your models here.

"""笔记"""
class NoteAdmin(admin.ModelAdmin):  
    list_display = ['id', 'title'] 

"""标签"""
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tagname']

"""专栏"""
class NotebookColumnAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title']

"""用户收藏笔记"""
class UserFavoriteNoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'note']

admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(NotebookColumn, NotebookColumnAdmin)
admin.site.register(UserFavoriteNote, UserFavoriteNoteAdmin)