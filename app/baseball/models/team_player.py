from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .player import Player
from .competition_team import CompetitionTeam, validate_team_jersey_number

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
    jersey_number = models.PositiveSmallIntegerField(null=True, validators=[validate_team_jersey_number])
    batting_totals = models.JSONField(default=dict)
    fielding_totals = models.JSONField(default=dict)
    pitching_totals = models.JSONField(default=dict)
    baserunning_totals = models.JSONField(default=dict)
    joined_team = models.DateField(blank=True, null=True)
    left_team = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=False)

    # related models
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='stats_by_team')
    competition_team = models.ForeignKey(CompetitionTeam, on_delete=models.SET_NULL, null=True, related_name='roster')

    def __str__(self) -> str:
        string = str(self.player)
        if self.jersey_number:
            string += f' #{self.jersey_number}'
        return string