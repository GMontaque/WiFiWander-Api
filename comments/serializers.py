from rest_framework import serializers
from .models import Comments
from wifi_locations.models import WifiLocation

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    wifi_location = serializers.PrimaryKeyRelatedField(queryset=WifiLocation.objects.all())

    class Meta:
        model = Comments
        fields = ['user', 'wifi_location', 'comment_text', 'created_at']

        # should wifi location be included even though it is not used
        '''
        so in the front end code under the comment section the user visiting 
        the site will need to see the name of the user who wrote the comment, 
        when they added the omment and the body of the comment, they would not 
        need the wifi location name as the comment would be on that specific 
        wifi lcotion page
        '''
