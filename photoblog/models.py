# -*- coding: utf-8 -*-
"""
Models for photoblog application

"""
# Standard library
from PIL import Image
from datetime import datetime
# Django
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
# Thumbnail
from djDentonPhotoblog.photoblog.thumbs import ImageWithThumbsField

class Category(models.Model):
    """
    A photo category
    
    """
    # fields
    name = models.CharField(_(u'Libellé'), max_length=255)
    slug = models.SlugField(_(u'URI'), max_length=255, unique=True)
    created_at = models.DateTimeField(_(u'Date de création'), auto_now_add=True)

    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save()
    
    class Meta:
        db_table = 'dj_categories'
        ordering = ['name']
        verbose_name = _(u'Catégorie')
        verbose_name_plural = _(u'Catégories')

class PhotoManager(models.Manager):
    
    def get_query_set(self):
        return super(PhotoManager, self).get_query_set().filter(is_published=True)
     
class Photo(models.Model):
    """
    A photo
    
    """
    # fields
    title = models.CharField(_(u'Titre'), max_length=255)
    slug = models.SlugField(_(u'URI'), max_length=255, unique=True)
    summary = models.TextField(_(u'Description'), null=True, blank=True)
    file = ImageWithThumbsField(_(u'Fichier'), upload_to='photos',
        height_field='file_height', width_field='file_width', sizes=((125,125),(200,200), (920, 760)))
    file_width = models.IntegerField(_(u'Largeur'), null=True, blank=True)
    file_height = models.IntegerField(_(u'Hauteur'), null=True, blank=True)
    is_published = models.BooleanField(_(u'Publié?'), null=False, default=True)
    created_at = models.DateTimeField(_(u'Date de création'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'Date de modification'), auto_now=True)
    category = models.ForeignKey(Category, verbose_name=_(u'Catégorie'))
    
    objects = models.Manager()
    public_objects = PhotoManager()
    
    @models.permalink
    def get_absolute_url(self):
        return ('photoblog_photo', (), {
            'category': self.category.slug,
            'slug': self.slug,
        })
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)        
        super(Photo, self).save()
        
    class Meta:
        db_table = 'dj_photos'
        ordering = ['-created_at']
        verbose_name = _(u'Photo')
        verbose_name_plural = _(u'Photos')

class EntryOnlineManager(models.Manager):
    """
    Manager that manages online ``Entry`` objects.
    """

    def get_query_set(self):
        return super(EntryOnlineManager, self).get_query_set().filter(
            status=self.model.STATUS_ONLINE)


class Entry(models.Model):
    """
    Actu
    """
    STATUS_OFFLINE = 0
    STATUS_ONLINE = 1
    STATUS_DEFAULT = STATUS_OFFLINE
    STATUS_CHOICES = (
        (STATUS_OFFLINE, _('Offline')),
        (STATUS_ONLINE, _('Online')),
    )

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique_for_date='publication_date')
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    modification_date = models.DateTimeField(_('modification date'), auto_now=True)
    publication_date = models.DateTimeField(_('publication date'), default=datetime.now(), db_index=True)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_DEFAULT, db_index=True)
    body = models.TextField(_('body'))

    objects = models.Manager()
    online_objects = EntryOnlineManager()

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_entry', (), {
            'year': self.publication_date.strftime('%Y'),
            'month': self.publication_date.strftime('%m'),
            'day': self.publication_date.strftime('%d'),
            'slug': self.slug,
        })


    
    