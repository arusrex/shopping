from typing import Any
from django.contrib import admin
from .models import Tag, Catergory, Page, Post, ImagesPost, News, ImageNew, Events, ImageEvent
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = "id", "name", "slug"
    list_per_page = 10

@admin.register(Catergory)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
    search_fields = "id", "name", "slug"
    list_per_page = 10
    ordering = ('name'),

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', 'title', 'slug', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('title', 'is_published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ["title"]
    search_fields = "id", "title", "slug", 'is_published'
    list_per_page = 10
    ordering = ('-id'),



class PostImageInline(admin.TabularInline):
    model = ImagesPost
    extra = 1

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', 'title', 'number', 'is_published', 'created_at', 'updated_at',)
    list_editable = ('is_published',)
    list_filter = ('title', 'category', 'is_published', 'number')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ["title"]
    search_fields = "id", "title", "slug", 'is_published', 'number',
    list_per_page = 30
    ordering = ('id'),
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by'
    filter_horizontal = ('tags',)
    inlines = [PostImageInline,]

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)
    


class NewsImageInline(admin.TabularInline):
    model = ImageNew
    extra = 1

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', 'is_published', 'title', 'short_description', 'created_at', 'updated_at',)
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('id', 'created_at', 'updated_at',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'short_description', 'description', 'created_at', 'updated_at',)
    ordering = ('-id',)
    inlines = [NewsImageInline,]
    


class EventsImageInline(admin.TabularInline):
    model = ImageEvent
    extra = 1

@admin.register(Events)
class EventsAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('id', 'is_published', 'title', 'short_description', 'created_at', 'updated_at',)
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('id', 'created_at', 'updated_at',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('id', 'title', 'short_description', 'description', 'created_at', 'updated_at',)
    ordering = ('-id',)
    inlines = [EventsImageInline,]