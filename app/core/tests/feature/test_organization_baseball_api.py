from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from core.models.user import User
from core.models.organization import Organization
from baseball.models.competition import Competition as BaseballCompetition
from baseball.models.choices.competition_type import CompetitionType as BaseballCompetitionType
from baseball.models.team import Team as BaseballTeam

class TestOrganizationBaseballCompetitionDetailsApi (APITestCase):
    """Tests for endpoints defined in the CompetitionDetails view.
    """
    fixtures = ['user', 'organization', 'competition']

    def setUp(self) -> None:
        """ Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='StatComplete')
        self.test_competition: BaseballCompetition = BaseballCompetition.objects.get(name='Test Season')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_baseball_competition_by_id(self):
        """Test the GET endpoint for getting a competition by its associated uuid.
        """
        response = self.client.get(f'/api/organizations/{self.test_organization.id}/baseball/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_competition.name, response.data.get('name'))
        self.assertEqual(self.test_competition.type, response.data.get('type'))

    def test_edit_baseball_competition(self):
        """Test the PATCH endpoint for editing a competition's info.
        """
        updated_competition_data = {
            'start_date':'2023-03-31',
        }
        response = self.client.patch(path=f'/api/organizations/{self.test_organization.id}/baseball/competitions/{self.test_competition.id}/', data=updated_competition_data, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_competition_data.get('start_date'), response.data.get('start_date'))
    

    def test_delete_baseball_competition(self):
        """Test the DELETE endpoint for deleting a competition by its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/organizations/{self.test_organization.id}/baseball/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/organizations/{self.test_organization.id}/baseball/competitions/{self.test_competition.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestOrganizationBaseballCompetitionListApi (APITestCase):
    """Tests for endpoints defined in the CompetitionList view.
    """
    fixtures = ['user', 'organization', 'competition']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_organization: Organization = Organization.objects.get(name='StatComplete')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_create_baseball_competition(self):
        """Test the POST endpoint for creating a competition.
        """
        competition_data = {
            'name' : 'Test Season',
            'type' : BaseballCompetitionType.SEASON
        }
        response = self.client.post(f'/api/organizations/{self.test_organization.id}/baseball/competitions/', data=competition_data, format='json')
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(competition_data.get('name'), response.data.get('name'))
        self.assertEqual(competition_data.get('type'), response.data.get('type'))

    def test_baseball_competitions_list(self):
        """Test the GET endpoint for getting the list of competitions.
        """
        response = self.client.get(f'/api/organizations/{self.test_organization.id}/baseball/competitions/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

class TestOrganizationBaseballTeamDetailsApi (APITestCase):
    """Tests for endpoints defined in TeamDetails view.
    """
    fixtures = ['user', 'organization', 'team']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_organization = Organization.objects.get(name='StatComplete')
        self.test_team = BaseballTeam.objects.get(location = 'Test', name = 'Team')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_baseball_team_by_id(self):
        """Test the GET endpoint for getting a team by its associated uuid.
        """
        response = self.client.get(path=f'/api/organizations/{self.test_organization.id}/baseball/teams/{self.test_team.id}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.test_team.location, response.data.get('location'))
        self.assertEqual(self.test_team.name, response.data.get('name'))
    
    def test_edit_baseball_team(self):
        """Test the PATCH endpoint for editing a team's info.
        """
        updated_team_field = {
            'location':'Updated',
        }
        response = self.client.patch(path=f'/api/organizations/{self.test_organization.id}/baseball/teams/{self.test_team.id}/', data=updated_team_field, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(updated_team_field.get('location'), response.data.get('location'))
    
    def test_delete_baseball_team(self):
        """Test the DELETE endpoint for deleting a team using its associated uuid.
        """
        delete_response = self.client.delete(path=f'/api/organizations/{self.test_organization.id}/baseball/teams/{self.test_team.id}/')
        self.assertEqual(status.HTTP_204_NO_CONTENT, delete_response.status_code)

        get_response = self.client.get(path=f'/api/organizations/{self.test_organization.id}/baseball/teams/{self.test_team.id}/')
        self.assertEqual(status.HTTP_404_NOT_FOUND, get_response.status_code)

class TestOrganizationBaseballTeamListApi (APITestCase):
    """Tests for endpoints defined in TeamList view.
    """
    fixtures = ['user', 'organization', 'team']

    def setUp(self):
        """Set up necessary objects for testing.
        """
        self.test_organization = Organization.objects.get(name='StatComplete')
        BaseballTeam.objects.get(location='Test', name='Team')
        BaseballTeam.objects.get(location='Another', name='Team')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()

    def test_create_baseball_team(self):
        """Test the POST endpoint for creating a team.
        """
        team_data = {
            'location' : 'TEST',
            'name' : 'TEAM',
        }
        response = self.client.post(path=f'/api/organizations/{self.test_organization.id}/baseball/teams/', data=team_data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(team_data.get('location'), response.data.get('location'))
        self.assertEqual(team_data.get('name'), response.data.get('name'))

    def test_baseball_teams_list(self):
        """Test the GET endpoint for getting the list of teams.
        """
        response = self.client.get(path=f'/api/organizations/{self.test_organization.id}/baseball/teams/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))