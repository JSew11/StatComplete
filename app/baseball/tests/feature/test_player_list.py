from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.player import Player

class TestPlayerListApi (APITestCase):
    """Tests for endpoints defined in PlayerList view.
    """
    fixtures = ['user']

    def setUp(self):
        """Set up necessary objects for testing.
        """
        Player.objects.create(
            first_name = 'Test',
            last_name = 'Player',
        )
        Player.objects.create(
            first_name = 'Another',
            last_name = 'Player',
        )
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()

    def test_create_player(self):
        """Test the POST endpoint for creating a player.
        """
        player_data = {
            'first_name' : 'TEST',
            'last_name' : 'PLAYER',
        }
        response = self.client.post(path='/api/baseball/players/', data=player_data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(player_data.get('first_name'), response.data.get('first_name'))
        self.assertEqual(player_data.get('last_name'), response.data.get('last_name'))

    def test_players_list(self):
        """Test the GET endpoint for getting the list of players.
        """
        response = self.client.get(path='/api/baseball/players/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))