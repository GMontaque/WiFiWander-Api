from django.db import models
from django.contrib.auth.models import User
from wifi_locations.models import WifiLocation


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wifi_location = models.ForeignKey(WifiLocation, on_delete=models.CASCADE)
    comment_text = models.TextField(null=True)
    star_rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.wifi_location.name}'
