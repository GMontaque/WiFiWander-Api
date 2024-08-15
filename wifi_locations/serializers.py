from rest_framework import serializers
from .models import WifiLocation,Address

class LocationsSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='user.username')


    class Meta:
        model = WifiLocation
        fields = ['name','address','description','star_rating','amenities','added_by']

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['street','city','country','postcode']

