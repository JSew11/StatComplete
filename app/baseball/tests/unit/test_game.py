from django.test import TestCase

from baseball.models.game import Game
from baseball.models.team import Team
from baseball.models.competition_team import CompetitionTeam

class TestGameModel (TestCase):
    """Tests for the game model.
    """
    fixtures = ['organization', 'competition', 'team', 'game', 'competition_team', 'team_box_score']

    def setUp(self) -> None:
        self.test_home_team: Team = Team.objects.get(
            location='Test',
            name='Team'
        )
        self.test_home_competition_team: CompetitionTeam = CompetitionTeam.objects.get(team=self.test_home_team)
        self.test_away_team: Team = Team.objects.get(
            location='Another',
            name='Team'
        )
        self.test_away_competition_team: CompetitionTeam = CompetitionTeam.objects.get(team=self.test_away_team)
        self.test_game: Game = Game.objects.get(id='301f4c55-beaf-4435-ade3-5c83833888c1')
        self.test_competition_game: Game = Game.objects.get(id='d2186785-cb0b-463e-a346-436bbdb8cfa6')
        return super().setUp()
    
    def test_game_string(self):
        """Test the overwritten __str__ method for the game model.
        """
        game_string_representation = f'{self.test_away_team} at {self.test_home_team} : {self.test_game.date}'
        self.assertEqual(game_string_representation, str(self.test_game))

    def test_home_team_property(self):
        """Test the home_team property of the game model.
        """
        self.assertEqual(self.test_home_competition_team, self.test_game.home_team)
        self.assertIsNone(self.test_competition_game.home_team)

    def test_add_team(self):
        """Test the add_team method for the game model.
        """
        message, success = self.test_game.add_team(self.test_home_competition_team, is_home_team=True)
        self.assertFalse(success)
        self.assertEqual('There are already 2 teams registered for this game.', message)
        
        _, success = self.test_competition_game.add_team(self.test_home_competition_team, is_home_team=True)
        self.assertTrue(success)

        message, success = self.test_competition_game.add_team(self.test_home_competition_team, is_home_team=True)
        self.assertFalse(success)
        self.assertEqual(message, f'CompetitionTeam \'{self.test_home_competition_team.id}\' is already added to this game.')

        message, success = self.test_competition_game.add_team(self.test_away_competition_team, is_home_team=True)
        self.assertFalse(success)
        self.assertEqual(message, 'There is already a home team in this game.')

        _, success = self.test_competition_game.add_team(self.test_away_competition_team, is_home_team=False)
        self.assertTrue(success)

    def test_get_opposing_team(self):
        """Test the get_opposing_team method for the game model.
        """
        self.assertEqual(self.test_away_competition_team, self.test_game.get_opposing_team(self.test_home_competition_team))
        self.assertIsNone(self.test_competition_game.get_opposing_team(self.test_home_competition_team))