from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from wifi_locations.models import WifiLocation

class WifiLocationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.wifi_location = WifiLocation.objects.create(
            name="Test Wifi Location",
            street="123 Test St",
            city="Test City",
            country="Test Country",
            postcode="12345",
            description="Test description",
            amenities="Test amenities",
            continent="Europe",
            added_by=self.user
        )
        self.client = APIClient()
    
    def test_get_wifi_locations_list(self):
        """
        Test retrieving the list of WiFi locations
        """
        response = self.client.get(reverse('wifi_location_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Wifi Location', response.data[0]['name'])
    
    def test_get_single_wifi_location(self):
        """
        Test retrieving a single WiFi location by ID
        """
        response = self.client.get(reverse('wifi_location_detail', kwargs={'pk': self.wifi_location.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.wifi_location.name)
    
    def test_create_wifi_location(self):
        """
        Test creating a new WiFi location
        """
        self.client.login(username='testuser', password='testpass')
        data = {
            'name': 'New Wifi Location',
            'street': '456 New St',
            'city': 'New City',
            'country': 'New Country',
            'postcode': '67890',
            'description': 'New description',
            'amenities': 'New amenities',
            'continent': 'Asia',
        }
        response = self.client.post(reverse('wifi_location_list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(WifiLocation.objects.count(), 2)
        self.assertEqual(response.data['name'], 'New Wifi Location')
    
    def test_update_wifi_location(self):
        """
        Test updating an existing WiFi location
        """
        self.client.login(username='testuser', password='testpass')
        data = {
            'name': 'Updated Wifi Location',
            'street': self.wifi_location.street,
            'city': self.wifi_location.city,
            'country': self.wifi_location.country,
            'postcode': self.wifi_location.postcode,
            'description': 'Updated description',
            'amenities': self.wifi_location.amenities,
            'continent': self.wifi_location.continent,
        }
        response = self.client.put(reverse('wifi_location_detail', kwargs={'pk': self.wifi_location.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wifi_location.refresh_from_db()
        self.assertEqual(self.wifi_location.name, 'Updated Wifi Location')
    
    def test_delete_wifi_location(self):
        """
        Test deleting a WiFi location
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('wifi_location_detail', kwargs={'pk': self.wifi_location.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(WifiLocation.objects.count(), 0)
    
    def test_cannot_create_duplicate_wifi_location(self):
        """
        Test that creating two Wi-Fi locations with the same name is not allowed
        """
        self.client.login(username='testuser', password='testpass')

        data = {
            'name': 'Test Wifi Location',
            'street': '456 New St',
            'city': 'New City',
            'country': 'New Country',
            'postcode': '67890',
            'description': 'New description',
            'amenities': 'New amenities',
            'continent': 'Asia',
        }

        response = self.client.post(reverse('wifi_location_list'), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertEqual(response.data['name'][0], 'wifi location with this name already exists.')
