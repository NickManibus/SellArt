from django.contrib import admin
from home.models import FeedBackContact, Work, Tags, Video
from django.utils.html import mark_safe
from embed_video.admin import AdminVideoMixin

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'active')


class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'thumbnail_preview', 'is_moderated')
    list_filter = ('title', 'is_moderated',)
    readonly_fields = ('thumbnail_preview', 'time_create', 'time_update',)
    search_fields = ('phone', 'email', 'title', 'author__username', 'author__first_name', 'author__last_name', 'video')
    prepopulated_fields = {"slug": ("title",)}

    def thumbnail_preview(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")
        return "-"

    thumbnail_preview.short_description = 'Preview'
    thumbnail_preview.allow_tags = True


class WorksVideo(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'name', 'email')
    list_filter = ('title', 'name', 'email', 'file')
    search_fields = ('title', 'name', 'email',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Work, WorksAdmin)
admin.site.register(Video, WorksVideo)
admin.site.register(FeedBackContact, ContactAdmin)
admin.site.register(Tags)
