from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class UrlModel(models.Model):
	url_title = models.URLField()
	url_description = models.TextField()

	def __repr__(self):
		return self.url_title


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)