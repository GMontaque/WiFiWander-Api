from rest_framework import serializers
from .models import Favourites
from wifi_locations.models import WifiLocation

class FavouritesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    wifi_location_name = serializers.ReadOnlyField(source='wifi_location.name')
    wifi_location_image = serializers.ImageField(source='wifi_location.image', read_only=True)
    wifi_location_id = serializers.PrimaryKeyRelatedField(
        queryset=WifiLocation.objects.all(),
        source='wifi_location',  # Ensure this is linked to the related model
        write_only=True
    )
    wifi_location_id_display = serializers.ReadOnlyField(source='wifi_location.id')  # Add this field to return the ID

    class Meta:
        model = Favourites
        fields = [
            'id', 'user', 'wifi_location_id', 'wifi_location_id_display',  # Ensure both are included
            'wifi_location_name', 'wifi_location_image', 'added_at', 
            'notes', 'folder_name', 'visit_status'
        ]
        read_only_fields = ['user', 'added_at']
