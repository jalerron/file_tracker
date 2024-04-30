from django.contrib import admin
from django.utils.html import format_html

from files.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'file', 'is_send',]
    exclude = ['is_send', 'title']
    list_display = ['title', 'status', 'date', 'is_send']
    ordering = ['date',]
    list_filter = ['status', 'date']


    # def active_checkbox(self, obj):
    #     return format_html('<input type="checkbox" {} disabled>', 'checked' if obj.active else '')
    #
    # active_checkbox.short_description = 'Active'

