from typing import Any
from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class PlayerFieldingStatsManager (models.Manager):
    """Manager for player fielding stats models.
    """
    def create(self, **kwargs: Any) -> Any:
        """Overridden create method to create associated models.
        """
        return super().create(**kwargs)

class PlayerFieldingStats (SafeDeleteModel):
    """Model for an individual player's fielding stats.
    
    Tracks standard counted fielding stats, separated by position.
    """
    objects = PlayerFieldingStatsManager()

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
