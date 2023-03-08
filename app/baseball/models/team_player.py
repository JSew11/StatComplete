from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .competition_player import CompetitionPlayer
from .competition_team import CompetitionTeam

class TeamPlayer (SafeDeleteModel):
    """Mode for a baseball player's stats as a part of a specific team.
    
    Tracks the player's stats and time as a part of the associated team.
    Includes the related competition player and competition team.
    """

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

    # related models
    competition_player = models.ForeignKey(CompetitionPlayer, on_delete=models.SET_NULL, null=True, related_name='stats_by_team')
    competition_team = models.ForeignKey(CompetitionTeam, on_delete=models.SET_NULL, null=True, related_name='player_stats')