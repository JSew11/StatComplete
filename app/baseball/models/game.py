from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .competition import Competition
from .competition_team import CompetitionTeam
from .choices.game_status import GameStatus

class Game (SafeDeleteModel):
    """Model for a baseball game.
    
    Includes the game details (start time, venue, status, rules) and associated
    competition.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # game info
    date = models.DateTimeField(blank=True, null=True)
    venue = models.JSONField(default=dict, blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        choices=GameStatus.choices,
        default=GameStatus.SCHEDULED
    )
    rules = models.JSONField(default=dict, blank=True, null=True)

    # related models
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name='schedule', null=True)

    def __str__(self) -> str:
        if self.teams.count() == 2:
            return f'{self.away_team.team} at {self.home_team.team} : {self.date}'
        return f'Game at {self.date}'
    
    @property
    def home_team(self) -> CompetitionTeam:
        return self.teams.filter(is_home_team=True).first().competition_team
    
    @property
    def away_team(self) -> CompetitionTeam:
        return self.teams.filter(is_home_team=False).first().competition_team
    
    def get_opposing_team(self, competition_team: CompetitionTeam) -> CompetitionTeam | None:
        """Get the opposing team for the given team.
        """
        try:
            return self.teams.filter(competition_team=competition_team).exclude()
        except CompetitionTeam.DoesNotExist:
            return None
        
    def save(self, keep_deleted=False, **kwargs):
        self.full_clean()
        return super().save(keep_deleted, **kwargs)

def limit_teams(game_id: str):
    if Game.objects.filter(id=game_id).count() >= 2:
        raise ValidationError('No more than 2 teams can play in a game')