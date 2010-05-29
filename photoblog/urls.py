# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from photoblog.feeds import LatestPhotosFeed

urlpatterns = patterns('',
    url(r'^feeds/latest/$', LatestPhotosFeed(), name='photoblog_latest_feed'),
    url(r'^archives/$', 'photoblog.views.archives', name='photoblog_archives'),
    url(r'^(?P<category>.*)/(?P<slug>.*).html$', 'photoblog.views.photo', name='photoblog_photo'),
    url(r'^$', 'photoblog.views.index', name='photoblog_home'),
)