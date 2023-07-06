from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models.user import User
from baseball.models.player import Player

class TestPlayerDetailsApi (APITestCase):
    """Tests for endpoints defined in PlayerDetails view.
    """
    fixtures = ['organization', 'user', 'player']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_player = Player.objects.get(first_name='Test', last_name='Player')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_player_by_id(self):
        """Test the GET endpoint for getting a player by its associated uuid.
        """
        response = self.client.get(path=f'/api/baseball/players/{self.test_player.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_player.first_name, response.data.get('first_name'))
        self.assertEqual(self.test_player.last_name, response.data.get('last_name'))
    
    def test_edit_player(self):
        """Test the PATCH endpoint for editing a player's info.
        """
        updated_player_field = {
            'birth_date':'2000-01-01',
        }
        response = self.client.patch(path=f'/api/baseball/players/{self.test_player.id}/', data=updated_player_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_player_field.get('birth_date'), response.data.get('birth_date'))
    
    def test_delete_player(self):
        """Test the DELETE endpoint for deleting a player using its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/players/{self.test_player.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/playeres/{self.test_player.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestPlayerListApi (APITestCase):
    """Tests for endpoints defined in PlayerList view.
    """
    fixtures = ['organization', 'user', 'player']

    def setUp(self):
        """Set up necessary objects for testing.
        """
        Player.objects.get(first_name = 'Test', last_name = 'Player')
        Player.objects.get(first_name='Another', last_name='Player')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
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