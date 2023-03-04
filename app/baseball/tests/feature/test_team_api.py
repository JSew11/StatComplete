from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.team import Team

class TestTeamDetailsApi (APITestCase):
    """Tests for endpoints defined in TeamDetails view.
    """
    fixtures = ['user', 'team']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_team = Team.objects.get(location = 'Test', name = 'Team')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_team_by_id(self):
        """Test the GET endpoint for getting a team by its associated uuid.
        """
        response = self.client.get(path=f'/api/baseball/teams/{self.test_team.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_team.location, response.data.get('location'))
        self.assertEqual(self.test_team.name, response.data.get('name'))
    
    def test_edit_team(self):
        """Test the PUT endpoint for editing a team's info.
        """
        updated_team_field = {
            'location':'Updated',
        }
        response = self.client.put(path=f'/api/baseball/teams/{self.test_team.id}/', data=updated_team_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_team_field.get('location'), response.data.get('location'))
    
    def test_delete_team(self):
        """Test the DELETE endpoint for deleting a team using its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/baseball/teams/{self.test_team.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/baseball/teames/{self.test_team.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestTeamListApi (APITestCase):
    """Tests for endpoints defined in TeamList view.
    """
    fixtures = ['user', 'team']

    def setUp(self):
        """Set up necessary objects for testing.
        """
        Team.objects.get(location='Test', name='Team')
        Team.objects.get(location='Another', name='Team')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()

    def test_create_team(self):
        """Test the POST endpoint for creating a team.
        """
        team_data = {
            'location' : 'TEST',
            'name' : 'TEAM',
        }
        response = self.client.post(path='/api/baseball/teams/', data=team_data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(team_data.get('location'), response.data.get('location'))
        self.assertEqual(team_data.get('name'), response.data.get('name'))

    def test_teams_list(self):
        """Test the GET endpoint for getting the list of teams.
        """
        response = self.client.get(path='/api/baseball/teams/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))