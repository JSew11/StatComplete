from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.team import Team

class TestTeamDetailsApi (APITestCase):
    """Tests for endpoints defined in TeamDetails view.
    """
    fixtures = ['user']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_team = Team.objects.create(
            location = 'Test',
            name = 'Team',
        )
        self.test_team_id = self.test_team.id
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_team_by_id(self):
        """Test the GET endpoint for getting a team by its associated uuid.
        """
        response = self.client.get(path=f'/api/baseball/teams/{self.test_team_id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_team.location, response.data.get('location'))
        self.assertEqual(self.test_team.name, response.data.get('name'))
    
    def test_edit_team(self):
        """Test the PUT endpoint for editing a team's info.
        """
        updated_team_field = {
            'location':'Updated',
        }
        response = self.client.put(path=f'/api/baseball/teams/{self.test_team_id}/', data=updated_team_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_team_field.get('location'), response.data.get('location'))
    
    def test_delete_team(self):
        """Test the DELETE endpoint for deleting a team using its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/teams/{self.test_team_id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/teames/{self.test_team_id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)