from django.db import models
from django.contrib.auth.models import User
from wifi_locations.models import WifiLocation

class Possibles(models.Model):
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
    visit_status = models.CharField(
        max_length=50,
        choices=VISIT_STATUS_CHOICES,
        default=PLANNED
    )
    notes = models.TextField(blank=True)
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=NA
    )

    class Meta:
        ordering = ['-added_at']
    
    def __str__(self):
        return f'{self.wifi_location.name} has been saved to {self.user.username}\'s Possibles list'

    '''
    •    id (Primary Key, int)
    •    user_id (Foreign Key to user profile, int)
    •    wifi_location_id (Foreign Key to wifi location, int)
    •    added_at (Date, auto-set when added)
    •    visit_status (Char, e.g., 'Planned', 'Visited')
    •    notes (Char, optional)
    •    priority (Int, e.g., 0 = N/A, 1 = Low, 2 = Medium, 3 = High)
    '''
