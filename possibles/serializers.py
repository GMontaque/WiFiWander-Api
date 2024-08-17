from rest_framework import serializers
from .models import Possibles
from wifi_locations.models import WifiLocation

class PossiblesSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    wifi_location = serializers.PrimaryKeyRelatedField(queryset=WifiLocation.objects.all())  # Allow setting during creation
    added_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Possibles
        fields = ['user', 'wifi_location', 'added_at', 'visit_status', 'notes', 'priority']
        read_only_fields = ['user', 'added_at']

