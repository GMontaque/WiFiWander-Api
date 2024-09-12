from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from wifi_locations.models import WifiLocation
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    created_at = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    wifi_location = serializers.PrimaryKeyRelatedField(queryset=WifiLocation.objects.all())

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Comments
        fields = ['id', 'user', 'comment_text', 'star_rating', 'created_at', 'is_owner', 'wifi_location']
