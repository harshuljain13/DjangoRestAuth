from rest_framework import serializers
from homeapp.models import NotesModel

class NotesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = NotesModel
		fields = ('id', 'note_title', 'note_description')