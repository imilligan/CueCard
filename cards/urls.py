from django.conf.urls import patterns, url

from cards import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^create/$', views.CreateView.as_view(), name='create'),
		url(r'^create/$', views.create, name='create'),
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)