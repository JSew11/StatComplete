from typing import Any
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class PlayerFieldingStats (SafeDeleteModel):
    """Model for an individual player's fielding stats.
    
    Tracks standard counted fielding stats, separated by position.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Fielding Stats'
        verbose_name_plural = 'Player Fielding Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def update_stats_by_position(self, position: int, stats: dict) -> bool:
        """Update the player's fielding stats for a specific position by adding the
        given value to the current stat value.
        """
        try:
            fielding_stats_by_position, _ = self.stats_by_position.get_or_create(position=position)
            for name, stat in stats.items():
                try :
                    prev_val = getattr(fielding_stats_by_position, name)
                    setattr(fielding_stats_by_position, name, (prev_val+stat))
                except Exception:
                    continue
            fielding_stats_by_position.save()
            return True
        except ValidationError:
            return False
