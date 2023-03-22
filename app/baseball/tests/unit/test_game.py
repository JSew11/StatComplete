from django.test import TestCase

from baseball.models.game import Game
from baseball.models.team import Team

class TestGameModel (TestCase):
    """Tests for the game model.
    """
    fixtures = ['organization', 'competition', 'team', 'game', 'competition_team', 'team_box_score']

    def setUp(self) -> None:
        self.test_home_team: Team = Team.objects.get(
            location='Test',
            name='Team'
        )
        self.test_away_team: Team = Team.objects.get(
            location='Another',
            name='Team'
        )
        self.test_game: Game = Game.objects.get(id='301f4c55-beaf-4435-ade3-5c83833888c1')
        return super().setUp()
    
    def test_game_string(self):
        """Test the overwritten __str__ method for the game model.
        """
        game_string_representation = f'{self.test_away_team} at {self.test_home_team} : {self.test_game.date}'
        self.assertEqual(game_string_representation, str(self.test_game))