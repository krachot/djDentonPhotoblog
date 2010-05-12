# -*- coding: utf-8 -*-
"""
Administration interface options of ``photoblog`` application.

"""
# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Application
from djDentonPhotoblog.photoblog.models import Category
from djDentonPhotoblog.photoblog.models import Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Category, CategoryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'summary', 'category')
    date_hierarchy = 'created_at'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Photo, PhotoAdmin)
