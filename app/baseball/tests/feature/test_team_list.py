from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.team import Team

class TestTeamListApi (APITestCase):
    """Tests for endpoints defined in TeamList view.
    """
    fixtures = ['user']

    def setUp(self):
        """Set up necessary objects for testing.
        """
        Team.objects.create(
            location = 'Test',
            name = 'Team',
        )
        Team.objects.create(
            location = 'Another',
            name = 'Team',
        )
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
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