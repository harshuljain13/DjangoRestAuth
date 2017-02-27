from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework import generics

from tokenapp.models import UrlModel
from tokenapp.serializers import UrlSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class UrlList(generics.ListCreateAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = UrlModel.objects.all()
	serializer_class = UrlSerializer

class UrlDetail(generics.RetrieveUpdateDestroyAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = UrlModel.objects.all()
	serializer_class = UrlSerializer