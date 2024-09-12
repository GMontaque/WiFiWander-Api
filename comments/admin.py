from django.contrib import admin
from .models import Comments


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'wifi_location', 'comment_text', 'created_at'
    )
    search_fields = ('user__username', 'comment_text')
    list_filter = ('created_at',)
