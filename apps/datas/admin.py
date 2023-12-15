from django.contrib.admin import *
from .models import (
    URLs,
    Files,
    Text,
    Image,
    Video
)

@register(URLs)
class URLsAdmin(ModelAdmin):
    list_display = ('id', 'description', 'date')
    list_display_links = ('id', 'description', 'date')
    ordering = ('-date',)
    exclude = ('date',)

@register(Files)
class FilesAdmin(ModelAdmin):
    list_display = ('id', 'description', 'date')
    list_display_links = ('id', 'description', 'date')
    ordering = ('-date',)
    exclude = ('date',)

@register(Text)
class TextAdmin(ModelAdmin):
    list_display = ('id', 'description', 'date')
    list_display_links = ('id', 'description', 'date')
    ordering = ('-date',)
    exclude = ('date',)

@register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ('id', 'description', 'date')
    list_display_links = ('id', 'description', 'date')
    ordering = ('-date',)
    exclude = ('date',)

@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('id', 'description', 'date')
    list_display_links = ('id', 'description', 'date')
    ordering = ('-date',)
    exclude = ('date',)