from typing import Any
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class PlayerBattingStats (SafeDeleteModel):
    """Model for an individual player's batting stats.
    
    Tracks standard counted batting stats, separated by lineup spot (location in
    the batting order).
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Batting Stats'
        verbose_name_plural = 'Player Batting Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def update_stats_by_lineup_spot(self, lineup_spot: int, stats: dict) -> bool:
        """Update the player's batting stats for a specific lineup spot by adding
        the given value to the current stat value.
        """
        try:
            batting_stats_by_lineup_spot, _ = self.stats_by_lineup_spot.get_or_create(lineup_spot=lineup_spot)
            for name, stat in stats.items():
                try :
                    prev_val = getattr(batting_stats_by_lineup_spot, name)
                    setattr(batting_stats_by_lineup_spot, name, (prev_val+stat))
                except Exception:
                    continue
            batting_stats_by_lineup_spot.save()
            return True
        except ValidationError:
            return False