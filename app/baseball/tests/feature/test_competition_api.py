from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from baseball.models.organization import Organization
from baseball.models.competition import Competition
from baseball.models.team import Team

class TestCompetitionDetailsApi (APITestCase):
    """Tests for details endpoints defined in the CompetitionViewSet.
    """
    fixtures = ['user', 'organization', 'competition']

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='Test Organization')
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_competition_by_id(self):
        """Test the GET endpoint for getting a competition by its associated uuid.
        """
        response = self.client.get(f'/api/baseball/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_competition.name, response.data.get('name'))
        self.assertEqual(self.test_competition.type, response.data.get('type'))

class TestCompetitionListApi (APITestCase):
    """Tests for list endpoints defined in the CompetitionViewSet.
    """
    fixtures = ['user', 'organization', 'competition']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_competitions_list(self):
        """Test the GET endpoint for getting the list of competitions.
        """
        response = self.client.get('/api/baseball/competitions/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

class TestCompetitionTeamApi (APITestCase):
    """Tests for competition team endpoints defined in the CompetitionViewset.
    """
    fixtures = ['user', 'organization', 'competition', 'team', 'competition_team']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.test_team: Team = Team.objects.get(location='Test', name='Team')
        self.client = APIClient()
        user = User.objects.get(username='DeveloperAdmin')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_register_team(self):
        """Test the POST endpoint for registering a team for a competition.
        """
        response = self.client.post(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_unregister_team(self):
        """Test the DELETE endpoint for unregistering a team from a competition.
        """
        response = self.client.delete(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)