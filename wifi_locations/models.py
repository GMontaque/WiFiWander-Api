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
    street = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=150, blank=False)
    country = models.CharField(max_length=150, blank=False)
    postcode = models.CharField(max_length=150, blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_q35ywj', null=True
    )
    description = models.TextField(blank=False)
    amenities = models.CharField(max_length=50, blank=False)
    continent = models.CharField(
        max_length=50, choices=CONTINENT_CHOICES, blank=False
    )
    added_by = models.ForeignKey(
        User, related_name='wifi_locations', null=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
