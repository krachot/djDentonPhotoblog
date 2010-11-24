# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf import settings

from photoblog.models import Photo

class LatestPhotosFeed(Feed):
    feed_type = Atom1Feed
    title = "Fiona Denton, latest photos"
    link = "/"
    description = "Updates on changes and additions to fiona.dentom.com"
    feed_copyright = 'Copyright (c) 2010, Fiona Denton'

    def items(self):
        return Photo.public_objects.order_by('-created_at')[:10]

    def item_title(self, item):
        return item.title

    def item_subtitle(self, item):
        return item.description
    
    def item_pubdate(self, item):
        return item.created_at

    def item_enclosure_url(self, item):
        return settings.NDD+item.file.url_920x760
    
    def item_enclosure_mime_type(self, item):
        return 'image/jpg'
    