from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .competition_team import CompetitionTeam
from .game import Game, limit_teams

class TeamBoxScore (SafeDeleteModel):
    """Model for a team's box score in a game.
    
    Includes the team's score, and total stats for the game. Also includes
    associated individual players' game stats.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Box Score'
        verbose_name_plural = 'Box Scores'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # box score info
    score_by_inning = models.JSONField(default=dict)
    batting_stats = models.JSONField(default=dict)
    fielding_stats = models.JSONField(default=dict)
    pitching_stats = models.JSONField(default=dict)
    baserunning_stats = models.JSONField(default=dict)
    is_home_team = models.BooleanField(default=False)

    # associated models
    competition_team = models.ForeignKey(CompetitionTeam, on_delete=models.SET_NULL, related_name='games', null=True)
    game = models.ForeignKey(Game, validators=(limit_teams, ), on_delete=models.SET_NULL, related_name='teams', null=True)