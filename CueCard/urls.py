from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from cards import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'sources', views.SourceViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CueCard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cards/', include('cards.urls', namespace="cards")),
    url(r'^admin/', include(admin.site.urls)),
)
