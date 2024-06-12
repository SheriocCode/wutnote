from rest_framework import serializers
from .models import Note, Tag

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'user','title', 'abstract', 'content', 
                  'tags', 'browse_num', 'favor_num', 'collect_num',
                'visibility', 'create_time', 'update_time','column')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tagname')