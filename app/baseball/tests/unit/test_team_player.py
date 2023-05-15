from django.test import TestCase

from baseball.models.constants import RIGHT_HANDED_MATCHUP
from baseball.models.choices.pitcher_role import PitcherRole
from baseball.models.choices.fielding_position import FieldingPosition
from baseball.models.team_player import TeamPlayer

class TestTeamPlayerModel (TestCase):
    """Tests for the team player model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 
                'player', 'team_player', 'player_baserunning_stats',
                'player_batting_stats',
                'player_pitching_stats', 'player_pitching_stats_by_role',
                'player_fielding_stats']

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

class TestPlayerBattingStatsModel (TestCase):
    """Tests for the player batting stats model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 
                'player', 'team_player', 'player_baserunning_stats',
                'player_batting_stats',
                'player_pitching_stats',
                'player_fielding_stats']
    
    def setUp(self) -> None:
        self.test_team_player: TeamPlayer = TeamPlayer.objects.get(
            player__first_name='Test',
            player__last_name='Player'
        )
        return super().setUp()
    
    def test_update_stats_by_lineup_spot(self):
        """Test the 'update_stats_by_lineup_spot' method of the player pitching stats model.
        """
        stat_updates = {
            'games_started': 6,
            'singles_vs_right': 4,
            'fake_stat': 194
        }
        updated = self.test_team_player.batting_stats.update_stats_by_lineup_spot(lineup_spot=2, stats=stat_updates)
        self.assertTrue(updated)
        self.assertEqual(6, self.test_team_player.batting_stats.games_started())


class TestPlayerPitchingStatsModel (TestCase):
    """Tests for the player pitching stats model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 
                'player', 'team_player', 'player_baserunning_stats',
                'player_batting_stats',
                'player_pitching_stats', 'player_pitching_stats_by_role',
                'player_fielding_stats']

    def setUp(self) -> None:
        self.test_team_player: TeamPlayer = TeamPlayer.objects.get(
            player__first_name='Test',
            player__last_name='Player'
        )
        return super().setUp()
    
    def test_wins(self):
        """Test the wins method of the player pitching stats model. Ensures the structure of
        the "cumulative stat methods" work as expected.
        """
        self.assertEqual(4, self.test_team_player.pitching_stats.wins([-1]))
        self.assertEqual(3, self.test_team_player.pitching_stats.wins([3, PitcherRole.STARTING_PITCHER]))
        self.assertEqual(1, self.test_team_player.pitching_stats.wins([PitcherRole.RELIEF_PITCHER]))
    
    def test_strikes_thrown(self):
        """Test the strikes_thrown method of the palyer pitching stats model. Ensures the
        structure of the "cumulative matchup stat methods" work as expected.
        """
        self.assertEqual(456, self.test_team_player.pitching_stats.strikes_thrown([-1], 'invalid'))
        self.assertEqual(321, self.test_team_player.pitching_stats.strikes_thrown([3], RIGHT_HANDED_MATCHUP))
        self.assertEqual(297, self.test_team_player.pitching_stats.strikes_thrown([PitcherRole.STARTING_PITCHER], RIGHT_HANDED_MATCHUP))

    def test_games_started(self):
        """Test the games_started property of the player pitching stats model.
        """
        self.assertEqual(7, self.test_team_player.pitching_stats.games_started)

    def test_innings_pitched(self):
        """Test the innings_pitched method of the player pitching stats model.
        """
        self.assertEqual(80/3, self.test_team_player.pitching_stats.innings_pitched())
        self.assertEqual(2.0, self.test_team_player.pitching_stats.innings_pitched(roles=[PitcherRole.RELIEF_PITCHER]))
        self.assertEqual(24.2, self.test_team_player.pitching_stats.innings_pitched(roles=[PitcherRole.STARTING_PITCHER], formatted=True))
    
    def test_earned_run_average(self):
        """Test the earned_run_average method of the player pitching stats model.
        """
        self.assertAlmostEqual(3.0375, self.test_team_player.pitching_stats.earned_run_average())

    def test_update_stats_by_role(self):
        """Test the 'update_stats_by_role' method of the player pitching stats model.
        """
        stat_updates = {
            'games_pitched': 2,
            'losses': 1,
            'fake_stat': 3
        }
        # invlid role
        updated = self.test_team_player.pitching_stats.update_stats_by_role(-1, stat_updates)
        self.assertFalse(updated)

        # valid role
        updated = self.test_team_player.pitching_stats.update_stats_by_role(PitcherRole.STARTING_PITCHER, stat_updates)
        self.assertTrue(updated)
        self.assertEqual(9, self.test_team_player.pitching_stats.games_started)
        self.assertEqual(9, self.test_team_player.pitching_stats.losses())

class TestPlayerFieldingStatsModel (TestCase):
    """Tests for the player fielding stats model.
    """
    fixtures = ['organization', 'competition', 'team', 'competition_team', 
                'player', 'team_player', 'player_baserunning_stats',
                'player_batting_stats',
                'player_pitching_stats',
                'player_fielding_stats']
    
    def setUp(self) -> None:
        self.test_team_player: TeamPlayer = TeamPlayer.objects.get(
            player__first_name='Test',
            player__last_name='Player'
        )
        return super().setUp()
    
    def test_update_stats_by_position(self):
        """Test the 'update_stats_by_position' method of the player fielding stats model.
        """
        stat_updates = {
            'games_started': 6,
            'putouts': 15,
            'fake_stat': 194
        }

        # invalid role
        updated = self.test_team_player.fielding_stats.update_stats_by_position(0, stat_updates)
        self.assertFalse(updated)

        updated = self.test_team_player.fielding_stats.update_stats_by_position(FieldingPosition.SECOND_BASE, stat_updates)
        self.assertTrue(updated)