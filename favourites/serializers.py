from rest_framework import serializers
from .models import Favourites
from wifi_locations.models import WifiLocation

class FavouritesSerializer(serializers.ModelSerializer):
    # check if user is required
    user = serializers.CharField(source='user.username', read_only=True)
    wifi_location = serializers.PrimaryKeyRelatedField(queryset=WifiLocation.objects.all())  # Allow setting during creation
    added_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Favourites
        fields = ['user', 'wifi_location', 'added_at','notes','folder_name','visit_status']
        read_only_fields = ['user', 'added_at']

