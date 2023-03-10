from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .player import Player
from .competition import Competition

class PlayerCompetitionStats (SafeDeleteModel):
    """Model for a baseball player's stats for a specific competition.

    Includes the related player and competition, as well as their stats for each
    team they played on as a part of that competition.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Stats'
        verbose_name_plural = 'Player Stats'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # related models
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stats_by_competition')
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name='players', null=True)