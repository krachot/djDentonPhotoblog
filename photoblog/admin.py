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
from djDentonPhotoblog.photoblog.models import Entry

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    save_on_top = True
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Category, CategoryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('get_thumbnail_img_tag', 'title', 'category', 'is_published', 'created_at', 'updated_at',)
    search_fields = ('title', 'summary', 'category',)
    list_filter = ('category',)
    list_display_links = ('title',)
    date_hierarchy = 'created_at'
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ('Photo', {
            'fields': ('category', 'file', 'title',)
        }),
        ('Options avancées', {
            'classes': ('collapse',),
            'fields': ('summary', 'is_published', 'slug')
        })
    )
    
    def get_thumbnail_img_tag(self, obj):
        return u'<img src="%s" />' % obj.file.url_125x125
    get_thumbnail_img_tag.short_description = 'Image'
    get_thumbnail_img_tag.allow_tags = True
    get_thumbnail_img_tag.admin_order_field = 'title'
    
admin.site.register(Photo, PhotoAdmin)

class EntryAdmin(admin.ModelAdmin):
    """
    Administration interface options of ``Entry`` model.
    """
    list_display = ('title', 'status')
    search_fields = ('title', 'body')
    date_hierarchy = 'publication_date'
    fieldsets = (
        (_('Headline'), {'fields': ('title', 'slug')}),
        (_('Publication'), {'fields': ('publication_date', 'status')}),
        (_('Body'), {'fields': ('body',)}),
    )
    save_on_top = True
    radio_fields = {'status': admin.VERTICAL}
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Entry, EntryAdmin)

