from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from wifi_locations.models import WifiLocation
from comments.models import Comments

class CommentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.wifi_location = WifiLocation.objects.create(name="Test Wifi Location")
        self.comment = Comments.objects.create(
            user=self.user,
            wifi_location=self.wifi_location,
            comment_text="Test comment",
            star_rating=4
        )
        self.client = APIClient()

    
    def test_get_comments_list(self):
        """
        Test retrieving the list of comments
        """
        response = self.client.get(reverse('comments-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test comment', response.data[0]['comment_text'])
    
    def test_get_comments_list_for_wifi_location(self):
        """
        Test retrieving the list of comments filtered by wifi_location
        """
        response = self.client.get(reverse('comments-list'), {'wifi_location': self.wifi_location.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['wifi_location'], self.wifi_location.id)
    
    def test_create_comment(self):
        """
        Test creating a new comment
        """
        self.client.login(username='testuser', password='testpass')
        data = {
            'comment_text': 'New test comment',
            'star_rating': 5,
            'wifi_location': self.wifi_location.id
        }
        response = self.client.post(reverse('comments-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comments.objects.count(), 2)
        self.assertEqual(response.data['comment_text'], 'New test comment')

    def test_get_single_comment(self):
        """
        Test retrieving a single comment
        """
        response = self.client.get(reverse('comments-detail', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment_text'], self.comment.comment_text)
    
    def test_update_comment(self):
        """
        Test updating a comment
        """
        self.client.login(username='testuser', password='testpass')
        data = {
            'comment_text': 'Updated comment text',
            'star_rating': 3,
            'wifi_location': self.wifi_location.id
        }
        response = self.client.put(reverse('comments-detail', kwargs={'pk': self.comment.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.comment_text, 'Updated comment text')
    
    def test_delete_comment(self):
        """
        Test deleting a comment
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('comments-detail', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comments.objects.count(), 0)

    def test_permission_required_for_post(self):
        """
        Ensure that creating a comment requires authentication
        """
        data = {
            'comment_text': 'Unauthorized comment',
            'star_rating': 3,
            'wifi_location': self.wifi_location.id
        }
        response = self.client.post(reverse('comments-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_required_for_delete(self):
        """
        Test that only the owner can delete a comment
        """
        another_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.delete(reverse('comments-detail', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

