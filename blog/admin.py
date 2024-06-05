from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'preview', 'views', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
