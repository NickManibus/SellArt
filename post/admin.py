from django.contrib import admin
from post.models import Post, Comment, Tags
from django.utils.html import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'thumbnail_preview', 'time_create', 'is_moderated')
    readonly_fields = ('thumbnail_preview', 'time_create', 'time_update',)
    list_filter = ('is_moderated', 'is_updated', 'status',)
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')
    prepopulated_fields = {'slug': ('title',)}

    def thumbnail_preview(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")
        return "-"

    thumbnail_preview.short_description = 'Preview'
    thumbnail_preview.allow_tags = True


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'is_moderated', 'created')
    search_fields = ('post', 'created', 'author__username', 'author__first_name', 'author__last_name')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tags)
