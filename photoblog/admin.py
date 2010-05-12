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
    list_display = ('get_thumbnail_img_tag', 'title', 'category', 'created_at', 'updated_at',)
    search_fields = ('title', 'summary', 'category',)
    list_filter = ('category',)
    list_display_links = ('title',)
    date_hierarchy = 'created_at'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    
    def get_thumbnail_img_tag(self, obj):
        return u'<img src="%s" />' % obj.file.url_125x125
    get_thumbnail_img_tag.short_description = 'Image'
    get_thumbnail_img_tag.allow_tags = True
    get_thumbnail_img_tag.admin_order_field = 'title'
    
admin.site.register(Photo, PhotoAdmin)
