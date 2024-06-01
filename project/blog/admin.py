from django.contrib import admin
from .models import Tag, Catergory, Page, Post, ImagesPost

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ["name"]
    search_fields = "id", "name", "slug"
    list_per_page = 10
    ordering = ['-id']

@admin.register(Catergory)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
    list_display_links = ["name"]
    search_fields = "id", "name", "slug"
    list_per_page = 10
    ordering = ('name'),

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
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
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'number', 'is_published', 'create_at', 'update_at',)
    list_editable = ('is_published',)
    list_filter = ('title', 'is_published', 'number')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ["title"]
    search_fields = "id", "title", "slug", 'is_published', 'number',
    list_per_page = 10
    ordering = ('id'),
    inlines = [PostImageInline,]