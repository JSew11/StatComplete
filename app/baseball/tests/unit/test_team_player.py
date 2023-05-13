from django.test import TestCase

from baseball.models.team_player import TeamPlayer

class TestTeamPlayerModel (TestCase):
    """Tests for the team player model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 
                'player', 'team_player', 'player_baserunning_stats',
                'player_pitching_stats', 'player_pitching_stats_by_role']

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

class TestPlayerPitchingStatsModel (TestCase):
    """Tests for the player pitching stats model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 
                'player', 'team_player', 'player_baserunning_stats',
                'player_pitching_stats', 'player_pitching_stats_by_role']

    def setUp(self) -> None:
        self.test_team_player: TeamPlayer = TeamPlayer.objects.get(
            player__first_name='Test',
            player__last_name='Player'
        )
        return super().setUp()
    
    def test_wins(self):
        """Test the wins method of the player pitching stats model.
        """
        self.assertEqual(4, self.test_team_player.pitching_stats.wins([-1]))
        self.assertEqual(3, self.test_team_player.pitching_stats.wins([3, 0]))
        self.assertEqual(1, self.test_team_player.pitching_stats.wins([1]))
    
    def test_games_started(self):
        """Test the games_started property of the player pitching stats model.
        """
        self.assertEqual(7, self.test_team_player.pitching_stats.games_started)
    
    def test_update_stats_by_role(self):
        """Test the 'update_stats_by_role' method of the player pitching stats manager.
        """
        stat_updates = {
            'games_played': 9,
            'games_pitched': 2,
            'losses': 1,
            'no-decisions': 3
        }
        # invlid role
        updated = self.test_team_player.pitching_stats.update_stats_by_role(-1, stat_updates)
        self.assertFalse(updated)

        # valid role
        updated = self.test_team_player.pitching_stats.update_stats_by_role(0, stat_updates)
        self.assertTrue(updated)
        self.assertEqual(9, self.test_team_player.pitching_stats.games_started)