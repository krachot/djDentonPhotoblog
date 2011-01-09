# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from photoblog.feeds import LatestPhotosFeed

from djDentonPhotoblog.photoblog.models import Entry

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-]+)/$',
       'django.views.generic.date_based.object_detail',
       dict(
           queryset=Entry.online_objects.all(),
           month_format='%m',
           date_field='publication_date',
           slug_field='slug',
       ),
       name='blog_entry',
    ),

    url(r'^news/$',
        'django.views.generic.date_based.archive_index',
        dict(
            queryset=Entry.online_objects.all(),
            date_field='publication_date',
        ),
        name='blog',
    ),
    url(r'^feeds/latest/$', LatestPhotosFeed(), name='photoblog_latest_feed'),
    url(r'^contact/$', 'photoblog.views.contact', name='photoblog_contact'),
    url(r'^archives/$', 'photoblog.views.archives', name='photoblog_archives'),
    url(r'^(?P<category>.*)/(?P<slug>.*).html$', 'photoblog.views.photo', name='photoblog_photo'),
    url(r'^$', 'photoblog.views.index', name='photoblog_home'),
)