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

    # check if user is required
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
        return f'{self.wifi_location.name} has been saved to {self.user.username}\'s favourites places to visit'

    '''
    •    id (Primary Key, int)
    •    user_id (Foreign Key to user profile, int)
    •    wifi_location_id (Foreign Key to wifi location, int)
    •    added_at (Date, auto-set when added)
    •    visit_status (Char, e.g., 'Planned', 'Visited')
    •    notes (Char, optional)
    '''
