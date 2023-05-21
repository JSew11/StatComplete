from rest_framework.test import APITestCase, APIClient
from rest_framework.response import Response
from rest_framework import status

from core.models.user import User
from baseball.models.organization import Organization
from baseball.models.competition import Competition
from baseball.models.team import Team
from baseball.models.competition_team import CompetitionTeam
from baseball.models.coach import Coach
from baseball.models.player import Player
from baseball.models.team_player import TeamPlayer

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
        user = User.objects.get(email='developer.admin@statcomplete.com')
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
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_competitions_list(self):
        """Test the GET endpoint for getting the list of competitions.
        """
        response = self.client.get('/api/baseball/competitions/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))

class TestCompetitionTeamListApi (APITestCase):
    """Tests for competition team endpoints defined in the CompetitionViewset.
    """
    fixtures = ['user', 'organization', 'competition', 'team', 'competition_team']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_list_teams(self):
        """Test the GET endpoint for viewing the competition's list of registered teams.
        """
        response = self.client.get(f'/api/baseball/competitions/{self.test_competition.id}/teams/')

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
        self.test_competition_team: CompetitionTeam = CompetitionTeam.objects.get(competition=self.test_competition, team=self.test_team)
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()

    def test_register_team(self):
        """Test the POST endpoint for registering a team for a competition.
        """
        response = self.client.post(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_retrieve_team(self):
        """Test the GET endpoint for getting the details of a specific competition team.
        """
        response = self.client.get(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(str(self.test_competition_team.id), response.data.get('id'))
    
    def test_update_competition_team_record(self):
        """Test the PATCH endpoint for updating a competition team's record.
        """
        response: Response = self.client.patch(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/', data={'wins': 1, 'losses': 2})

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, response.data['record']['wins'])
        self.assertEqual(2, response.data['record']['losses'])
        self.assertEqual(0, response.data['record']['ties'])

    def test_unregister_team(self):
        """Test the DELETE endpoint for unregistering a team from a competition.
        """
        response = self.client.delete(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

class TestTeamCoachApi (APITestCase):
    """Tests for team coach endpoints defined in the CompetitionViewSet.
    """
    fixtures = ['user', 'organization', 'competition', 'team', 'competition_team', 'coach', 'team_coach']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.test_team: Team = Team.objects.get(location='Test', name='Team')
        self.test_coach: Coach = Coach.objects.get(first_name='Test', last_name='Coach')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_add_team_coach(self):
        """Test the POST endpoint for adding a coach to a team's competition coaching staff.
        """
        test_coach_data = {
            'jersey_number': 1
        }
        response: Response = self.client.post(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/coaches/{self.test_coach.id}/', data=test_coach_data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
    
    def test_partial_update_team_coach(self):
        """Test the PATCH update for updating a team coach on a competition team's coaching staff.
        """
        test_coach_data = {
            'jersey_number': '2'
        }
        response: Response = self.client.patch(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/coaches/{self.test_coach.id}/', data=test_coach_data, format='json')

        self.assertEqual(status.HTTP_200_OK, response.status_code)
    
    def test_delete_team_coach(self):
        """Test the DELETE endpoint for removing a coach from a competition team's coaching staff.
        """
        response: Response = self.client.delete(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/coaches/{self.test_coach.id}/')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

class TestTeamPlayerApi (APITestCase):
    """Tests for team player endpoints defined in the competition viewset.
    """
    fixtures = ['user', 'organization', 'competition', 'team', 'competition_team',
                'player', 'team_player', 'player_baserunning_stats',
                'player_batting_stats',
                'player_pitching_stats', 'player_pitching_stats_by_role',
                'player_fielding_stats']

    def setUp(self) -> None:
        """Set up necessary objects for testing.
        """
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.test_team: Team = Team.objects.get(location='Test', name='Team')
        self.test_player: Player = Player.objects.get(first_name='Test', last_name='Player')
        self.test_team_player: TeamPlayer = TeamPlayer.objects.get(
            competition_team__competition=self.test_competition,
            competition_team__team = self.test_team,
            player=self.test_player
        )
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_create_team_player(self):
        """Test the POST endpoint for adding a player to a competition team's roster.
        """
        test_player_data = {
            'jersey_number': 1
        }
        response: Response = self.client.post(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/players/{self.test_player.id}/', data=test_player_data, format='json')

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_update_team_player_stats(self):
        """Test the PUT endpoint for updating a player's stats.
        """
        stat_updates = {
            'batting': {
                'stats_by_lineup_spot': {
                    1: {
                        'games_started': 6,
                        'singles_vs_right': 4,
                    },
                    3: {
                        'singles_vs_left': 6,
                    },
                },
            },
            'baserunning': {
                'games_pinch_run': 7,
                'steals_second_base': 5,
                'caught_stealing_second_base': 1,
                'steals_third_base': 1,
                'caught_stealing_third_base': 2,
            },
            'pitching': {
                'complete_games': 1,
                'holds': 1,
                'saves': 2,
                'save_opportunities': 3,
                'stats_by_role': {
                    0: {
                        'games_pitched': 2,
                        'losses': 1,
                    },
                },
            },
            'fielding': {
                'stats_by_position': {
                    3: {
                        'games_started': 6,
                        'putouts': 32,
                    },
                    6: {
                        'games_started': 2,
                        'assists': 10,
                    },
                },
            },
        }
        response = self.client.put(f'/api/baseball/competitions/{self.test_competition.id}/teams/{self.test_team.id}/players/{self.test_player.id}/', data={'stats': stat_updates}, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(6, self.test_team_player.batting_stats.games_started())
        self.assertEqual(10, self.test_team_player.batting_stats.singles())
        self.assertEqual(7, self.test_team_player.baserunning_stats.games_pinch_run)
        self.assertEqual(6, self.test_team_player.baserunning_stats.steals())
        self.assertEqual(1, self.test_team_player.pitching_stats.complete_games)
        self.assertEqual(9, self.test_team_player.pitching_stats.games_started)
        self.assertEqual(1, self.test_team_player.pitching_stats.losses())
        self.assertEqual(8, self.test_team_player.fielding_stats.games_started())
        self.assertEqual(32, self.test_team_player.fielding_stats.putouts())
        self.assertEqual(10, self.test_team_player.fielding_stats.assists())

class TestGameApi(APITestCase):
    """Tests for game endpoints defined in the competition viewset.
    """
    fixtures = ['user', 'organization', 'competition', 'team', 'competition_team']

    def setUp(self) -> None:
        self.test_competition: Competition = Competition.objects.get(name='Test Season')
        self.test_home_team: CompetitionTeam = CompetitionTeam.objects.get(id='ff829ff9-e0c4-4ba3-8ee2-5a391fd257bc')
        self.test_away_team: CompetitionTeam = CompetitionTeam.objects.get(id='b59e9d57-0e60-4da8-a023-32b37c2a1333')
        self.client = APIClient()
        user = User.objects.get(email='developer.admin@statcomplete.com')
        self.client.force_authenticate(user)
        return super().setUp()
    
    def test_create_game(self):
        """Test the POST endpoint for creating a game as a part of the given competition.
        """
        response: Response = self.client.post(f'/api/baseball/competitions/{self.test_competition.id}/games/')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        test_game_data = {
            'home_team': self.test_home_team.id,
            'away_team': self.test_away_team.id
        }
        response: Response = self.client.post(f'/api/baseball/competitions/{self.test_competition.id}/games/', data=test_game_data, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)