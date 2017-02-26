from django.conf.urls import url
from homeapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^notes/$',views.notesList.as_view(), name='notes-list'),
    url(r'^notes/(?P<pk>[0-9]+)/$', views.notesDetail.as_view(), name='notes-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)