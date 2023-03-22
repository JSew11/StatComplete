from django.test import TestCase

from baseball.models.team_player import TeamPlayer

class TestTeamPlayerModel (TestCase):
    """Tests for the team player model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 'player', 'team_player']

    def setUp(self) -> None:
        self.test_team_player: TeamPlayer = TeamPlayer.objects.get(
            player__first_name='Test',
            player__last_name='Player'
        )
        return super().setUp()
    
    def test_team_player_string(self):
        """Test the overwritten __str__ method for the team player model.
        """
        player_string_representation = str(self.test_team_player.player)+f' #{self.test_team_player.jersey_number}'
        self.assertEqual(player_string_representation, str(self.test_team_player))