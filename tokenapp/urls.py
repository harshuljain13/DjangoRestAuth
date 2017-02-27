from django.conf.urls import url
from tokenapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

urlpatterns = [
	url(r'^urls/$',views.UrlList.as_view(), name='url-list'),
    url(r'^urls/(?P<pk>[0-9]+)/$', views.UrlDetail.as_view(), name='url-detail'),
    url(r'^api-token-auth/$', rest_views.obtain_auth_token),
]
urlpatterns = format_suffix_patterns(urlpatterns)