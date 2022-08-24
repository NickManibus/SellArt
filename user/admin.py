from django.contrib import admin
from user.models import User
from home.models import Work

class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('username', 'email',)


admin.site.register(User, AdminUser)
