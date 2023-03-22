from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from ..models.team_player import TeamPlayer
from ..models.team_box_score import TeamBoxScore

class PlayerGameStats (SafeDeleteModel):
    """Model for a player's stats for a single game.
    
    Includes stats for: 
        - batting (tracked per pitch by plate appearance)
        - fielding (tracked per position)
        - pitching (tracked per pitch by plate appearance)
        - baserunning (tracked per action)
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Game Stats'
        verbose_name_plural = 'Player Game Stats'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # tracked stats
    batting = models.JSONField(default=dict)
    fielding = models.JSONField(default=dict)
    pitching = models.JSONField(default=dict)
    baserunning = models.JSONField(default=dict)

    # associated models
    team_player = models.ForeignKey(TeamPlayer, on_delete=models.SET_NULL, related_name='stats_by_game', null=True)
    game_box_score = models.ForeignKey(TeamBoxScore, on_delete=models.SET_NULL, related_name='lineup', null=True)