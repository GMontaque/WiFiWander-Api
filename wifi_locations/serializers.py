from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import WifiLocation,Address

class LocationsSerializer(serializers.ModelSerializer):

    added_by = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = WifiLocation
        fields = ['name','address','image','description','amenities','added_by','created_at','updated_at']

class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Address
        fields = ['id','street','city','country','postcode']

