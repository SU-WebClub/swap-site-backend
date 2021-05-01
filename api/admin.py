from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms import TextInput, Textarea
from django.db import models
from .models import (
    Category,
    Tag,
    Blog,
    Author,
    Role,
    News
)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview', 'created_at', 'category', 'is_public')
    list_filter = ('is_public',)
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))

    thumbnail_preview.short_description = 'サムネ'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('icon_preview', 'name')

    def icon_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.icon.url))


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_preview')

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))


admin.site.register(Blog, BlogAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Role)
admin.site.register(Author, AuthorAdmin)