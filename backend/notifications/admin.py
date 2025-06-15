from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'send_time')
    list_filter = ('type', 'status')
    search_fields = ('content',)
