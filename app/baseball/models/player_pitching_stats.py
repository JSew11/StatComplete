from typing import Any
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class PlayerPitchingStats(SafeDeleteModel):
    """Model for an individual player's pitching stats.
    
    Tracks standard counted pitching stats for a player, separated by role.
    """

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
        return self.stats_by_role.filter(role=0).first().games_pitched
    
    def update_stats_by_role(self, role: int, stats: dict, **kwargs: Any) -> bool:
        """Update the player's pitching stats for a specific role by adding the
        given value to the current stat value.
        """
        try:
            pitching_stats_by_role, _ = self.stats_by_role.get_or_create(role=role)
            for name, stat in stats.items():
                try :
                    prev_val = getattr(pitching_stats_by_role, name)
                    setattr(pitching_stats_by_role, name, (prev_val+stat))
                except Exception:
                    continue
            pitching_stats_by_role.save()
            return True
        except ValidationError:
            return False
