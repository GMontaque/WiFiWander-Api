from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    created_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Comments
        fields = ['user', 'comment_text','star_rating', 'created_at']

        # should wifi location be included even though it is not used
        '''
        so in the front end code under the comment section the user visiting 
        the site will need to see the name of the user who wrote the comment, 
        when they added the omment and the body of the comment, they would not 
        need the wifi location name as the comment would be on that specific 
        wifi lcotion page
        '''
