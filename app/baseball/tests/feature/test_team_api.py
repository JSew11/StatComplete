from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models.user import User
from baseball.models.team import Team

class TestTeamListApi (APITestCase):
    """Tests for endpoints defined in TeamList view.
    """
    fixtures = ['user', 'organization', 'team']

    def setUp(self):
        """Set up necessary objects for testing.
        """
        Team.objects.get(location='Test', name='Team')
        Team.objects.get(location='Another', name='Team')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_teams_list(self):
        """Test the GET endpoint for getting the list of teams.
        """
        response = self.client.get(path=f'/api/baseball/teams/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

class TestTeamDetailsApi (APITestCase):
    """Tests for endpoints defined in TeamDetails view.
    """
    fixtures = ['user', 'organization', 'team']

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