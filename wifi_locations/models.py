from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    postcode = models.CharField(max_length=150)

# Create your models here.
class WifiLocation(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, unique=True)
    image = models.ImageField(upload_to='images/', default='../default_profile_q35ywj',null=True)
    description = models.TextField()
    amenities = models.CharField(max_length=50, blank=False)
    added_by = models.ForeignKey(User, related_name='wifi_location', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

