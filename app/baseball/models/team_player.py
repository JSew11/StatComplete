from datetime import datetime
from typing import Any
from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .player import Player
from .player_batting_stats import PlayerBattingStats
from .player_baserunning_stats import PlayerBaserunningStats
from .player_pitching_stats import PlayerPitchingStats
from .player_fielding_stats import PlayerFieldingStats
from .competition_team import CompetitionTeam, validate_team_jersey_number

class TeamPlayerManager (models.Manager):
    """Manager for team player models.
    """
    def create(self, **kwargs: Any) -> Any:
        """Overridden create method to create associated models.
        """
        team_player: TeamPlayer = super().create(**kwargs)
        team_player.joined_team = datetime.now()
        team_player.active = True
        team_player.batting_stats = PlayerBattingStats.objects.create()
        team_player.baserunning_stats = PlayerBaserunningStats.objects.create()
        team_player.pitching_stats = PlayerPitchingStats.objects.create()
        team_player.fielding_stats = PlayerFieldingStats.objects.create()
        team_player.save()
        return team_player

class TeamPlayer (SafeDeleteModel):
    """Model for a baseball player's stats as a part of a specific team.
    
    Tracks the player's stats and time as a part of the associated team.
    Includes the related competition player and competition team.
    """
    objects = TeamPlayerManager()

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Stats (Team)'
        verbose_name_plural = 'Player Stats (Team)'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # team-specific info
    jersey_number = models.PositiveSmallIntegerField(null=True, validators=[validate_team_jersey_number])
    joined_team = models.DateTimeField(blank=True, null=True)
    left_team = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)

    # stats
    batting_stats = models.OneToOneField(PlayerBattingStats, on_delete=models.SET_NULL, null=True, related_name='team_player')
    baserunning_stats = models.OneToOneField(PlayerBaserunningStats, on_delete=models.SET_NULL, null=True, related_name='team_player')
    pitching_stats = models.OneToOneField(PlayerPitchingStats, on_delete=models.SET_NULL, null=True, related_name='team_player')
    fielding_stats = models.OneToOneField(PlayerFieldingStats, on_delete=models.SET_NULL, null=True, related_name='team_player')

    # related models
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='stats_by_team')
    competition_team = models.ForeignKey(CompetitionTeam, on_delete=models.SET_NULL, null=True, related_name='roster')

    def update_batting_stats(self, batting_stats: dict) -> None:
        """Update the player's batting stats using the given dict of batting stats.
        """
        batting_stats_by_lineup_spot: dict = batting_stats.pop('stats_by_lineup_spot', dict())
        for lineup_spot, stats_by_lineup_spot in batting_stats_by_lineup_spot.items():
            self.batting_stats.update_stats_by_lineup_spot(lineup_spot, stats_by_lineup_spot)
        self.batting_stats.save()

    def update_baserunning_stats(self, baserunning_stats: dict) -> None:
        """Update the player's baserunning stats using the given dict of baserunning stats.
        """
        for name, stat in baserunning_stats.items():
            try:
                prev_val = getattr(self.baserunning_stats, name)
                setattr(self.baserunning_stats, name, (prev_val+stat))
            except Exception:
                continue
        self.baserunning_stats.save()

    def update_pitching_stats(self, pitching_stats: dict) -> None:
        """Update the player's pitching stats using the given dict of pitching stats.
        """
        pitching_stats_by_role: dict = pitching_stats.pop('stats_by_role', dict())
        for name, stat in pitching_stats.items():
            try:
                prev_val = getattr(self.pitching_stats, name)
                setattr(self.pitching_stats, name, (prev_val+stat))
            except Exception:
                continue
        for role, stats_by_role in pitching_stats_by_role.items():
            self.pitching_stats.update_stats_by_role(role, stats_by_role)
        self.pitching_stats.save()

    def update_fielding_stats(self, fielding_stats: dict) -> None:
        """Update the player's fielding stats using the given dict of fielding stats.
        """
        fielding_stats_by_position: dict = fielding_stats.pop('stats_by_position', dict())
        for position, stats_by_position in fielding_stats_by_position.items():
            self.fielding_stats.update_stats_by_position(position, stats_by_position)
        self.fielding_stats.save()

    def update_all_stats(self, stats: dict) -> None:
        """Update the player's stats using the given stats data.
        """
        if batting_stats := stats['batting']:
            self.update_batting_stats(batting_stats=batting_stats)
        if baserunning_stats := stats['baserunning']:
            self.update_baserunning_stats(baserunning_stats=baserunning_stats)
        if pitching_stats := stats['pitching']:
            self.update_pitching_stats(pitching_stats=pitching_stats)
        if fielding_stats := stats['fielding']:
            self.update_fielding_stats(fielding_stats=fielding_stats)

    def __str__(self) -> str:
        string = str(self.player)
        if self.jersey_number:
            string += f' #{self.jersey_number}'
        return string