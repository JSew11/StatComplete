from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .player import Player

class PlayerStats (SafeDeleteModel):
    """Model for a baseball player's stats for a specific team.

    Includes the related player and team, a json object for games played by
    position, as well as json objects storing total stat data for fielding, 
    batting, pitching, etc. Also includes related stats yb game and the dates
    when the player started and finished (if applicable) with the associated
    team.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE
    PROTECTED_FIELDS = ['id', 'created', 'updated', 'deleted']

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Stats'
        verbose_name_plural = 'Player Stats'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # related models
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='stats_by_team')

    # stats/team-specific info
    jersey_number = models.PositiveSmallIntegerField(blank=True, null=True)
    games_played_by_position = models.JSONField(default=dict)
    stats = models.JSONField(default=dict)