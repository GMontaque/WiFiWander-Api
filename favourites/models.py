from django.db import models
from django.contrib.auth.models import User
from wifi_locations.models import WifiLocation


class Favourites(models.Model):
    PLANNED = 'Planned'
    VISITED = 'Visited'

    VISIT_STATUS_CHOICES = [
        (PLANNED, 'Planned'),
        (VISITED, 'Visited'),
    ]

    NA = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    PRIORITY_CHOICES = [
        (NA, 'N/A'),
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wifi_location = models.ForeignKey(WifiLocation, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(blank=True, max_length=300)
    folder_name = models.CharField(blank=True, max_length=300)
    visit_status = models.CharField(
        max_length=50,
        choices=VISIT_STATUS_CHOICES,
        default=PLANNED
    )

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return (
            f'{self.wifi_location.name} has been saved to '
            f"{self.user.username}'s favourites places to visit"
        )
