from rest_framework import serializers
from tokenapp.models import UrlModel

class UrlSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UrlModel
		fields = ('id', 'url_title', 'url_description')