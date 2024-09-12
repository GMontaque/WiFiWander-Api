from django.contrib import admin
from .models import Favourites


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'wifi_location', 'visit_status', 'added_at'
    )
    search_fields = (
        'user__username', 'wifi_location__name'
    )
    list_filter = (
        'visit_status', 'added_at'
    )
