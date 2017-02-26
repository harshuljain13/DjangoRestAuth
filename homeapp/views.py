from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework import generics

from homeapp.models import NotesModel
from homeapp.serializers import NotesSerializer
# Create your views here.


class notesList(generics.ListCreateAPIView):
	queryset = NotesModel.objects.all()
	serializer_class = NotesSerializer

class notesDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = NotesModel.objects.all()
	serializer_class = NotesSerializer