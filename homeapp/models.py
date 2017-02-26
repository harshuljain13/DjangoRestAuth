from __future__ import unicode_literals

from django.db import models

# Create your models here.


class NotesModel(models.Model):
	note_title = models.CharField(max_length=100)
	note_description = models.CharField(max_length=10000)

	def __repr__(self):
		return self.note_title