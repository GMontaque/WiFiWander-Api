from django.contrib import admin
from .models import WifiLocation

@admin.register(WifiLocation)
class WifiLocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','country','created_at', 'updated_at')
    search_fields = ('name', 'country')
    list_filter = ('created_at', 'updated_at')
