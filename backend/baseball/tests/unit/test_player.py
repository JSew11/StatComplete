from django.test import TestCase

from baseball.models.player import Player

class TestPlayerModel (TestCase):
    """Tests for the player model.
    """

    def setUp(self) -> None:
        self.test_player = Player.objects.create(
            first_name = 'Test',
            last_name = 'Player'
        )
        return super().setUp()
    
    def test_player_string(self):
        """Test the overwritten __str__ method for the player model.
        """
        player_string_representation = f'{self.test_player.first_name} {self.test_player.last_name}'
        self.assertEqual(player_string_representation, str(self.test_player))