from django.db import models
from django.contrib.auth.models import User

CONTINENT_CHOICES = [
    ('Africa', 'Africa'),
    ('Asia', 'Asia'),
    ('Europe', 'Europe'),
    ('North America', 'North America'),
    ('Australia', 'Australia'),
    ('South America', 'South America'),
]

class WifiLocation(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    street = models.CharField(max_length=150, blank=False, default='')
    city = models.CharField(max_length=150, blank=False, default='')
    country = models.CharField(max_length=150, blank=False, default='')
    postcode = models.CharField(max_length=150, blank=False, default='')
    image = models.ImageField(upload_to='images/', default='../default_profile_q35ywj', null=True)
    description = models.TextField(blank=False, default='')
    amenities = models.CharField(max_length=50, blank=False, default='')
    continent = models.CharField(max_length=50, choices=CONTINENT_CHOICES, blank=False, default='')
    added_by = models.ForeignKey(User, related_name='wifi_locations', null=True, on_delete=models.SET_NULL, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
