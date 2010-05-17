# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.conf import settings

from PIL import Image
from photoblog.models import Category, Photo

URL_BLOG = settings.NDD

def index(request, template_name='photoblog/index.html'):
    try:
        photo = Photo.public_objects.order_by('-created_at')[0]
    except IndexError:
        photo = None
    
    if photo:
        try:
            prev = photo.get_previous_by_created_at( is_published=1 )
        except Photo.DoesNotExist:
            prev = None
        
    data = {
        'photo': photo,
        'prev': prev,
        'ndd': URL_BLOG,
    }
    return render_to_response(template_name, data, RequestContext(request, {}))
    
def photo(request, category=None, slug=None, template_name='photoblog/photo.html'):
    photo = get_object_or_404(
        Photo,
        category__slug=category,
        slug=slug,
        is_published=1,
    )
    
    try:
        prev = photo.get_previous_by_created_at( is_published=1 )
    except Photo.DoesNotExist:
        prev = None
    
    try:
        next = photo.get_next_by_created_at( is_published=1 )
    except Photo.DoesNotExist:
        next = None
    
    data = {
        'photo': photo,
        'prev': prev,
        'next': next,
        'ndd': URL_BLOG,
    }
    
    return render_to_response(template_name, data, RequestContext(request, {}))

def archives(request, template_name='photoblog/archives.html'):
    data = {
        'archives': Photo.public_objects.order_by('category__name', 'created_at').all(),
    }
    return render_to_response(template_name, data, RequestContext(request, {}))
