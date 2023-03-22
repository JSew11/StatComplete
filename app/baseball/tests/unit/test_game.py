from django.test import TestCase

from baseball.models.game import Game

class TestGameModel (TestCase):
    """Tests for the game model.
    """
    fixtures = ['organization', 'competition', 'game']

    def setUp(self) -> None:
        self.test_game: Game = Game.objects.get(id='301f4c55-beaf-4435-ade3-5c83833888c1')
        return super().setUp()
    
    def test_game_string(self):
        """Test the overwritten __str__ method for the game model.
        """
        game_string_representation = f'Game at {self.test_game.date}'
        self.assertEqual(game_string_representation, str(self.test_game))