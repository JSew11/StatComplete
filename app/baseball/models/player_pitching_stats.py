from typing import Any
from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class PlayerPitchingStatsManager (models.Manager):
    """Manager for player pitching stats models.
    """
    def create(self, **kwargs: Any) -> Any:
        """Overridden create method to create associated models.
        """
        player_pitching_stats: PlayerPitchingStats = super().create(**kwargs)
        player_pitching_stats.stats_by_role.create(role=0)
        player_pitching_stats.stats_by_role.create(role=1)
        player_pitching_stats.save()
        return player_pitching_stats

class PlayerPitchingStats(SafeDeleteModel):
    """Model for an individual player's pitching stats.
    
    Tracks standard counted pitching stats for a player, separated by role.
    """
    objects = PlayerPitchingStatsManager()

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Pitching Stats'
        verbose_name_plural = 'Player Pitching Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # counted stats (cannot be tracked by role)
    complete_games = models.PositiveIntegerField(default=0)
    shutouts = models.PositiveIntegerField(default=0)
    holds = models.PositiveIntegerField(default=0)
    saves = models.PositiveIntegerField(default=0)
    save_opportunities = models.PositiveIntegerField(default=0)

    @property
    def games_started(self):
        return self.stats_by_role.filter(role=0).aggregate(models.Sum('games_pitched'))['games_pitched__sum']