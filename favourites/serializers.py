from rest_framework import serializers
from .models import Favourites
from wifi_locations.models import WifiLocation

class FavouritesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    wifi_location_name = serializers.CharField(source='wifi_location.name', read_only=True)
    wifi_location_image = serializers.ImageField(source='wifi_location.image', read_only=True)
    wifi_location_id = serializers.PrimaryKeyRelatedField(
        queryset=WifiLocation.objects.all(),
        source='wifi_location',
        write_only=True
    )
    added_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Favourites
        fields = [
            'id', 'user', 'wifi_location_id', 'wifi_location_name', 
            'wifi_location_image', 'added_at', 'notes', 'folder_name', 
            'visit_status'
        ]
        read_only_fields = ['user', 'added_at']
