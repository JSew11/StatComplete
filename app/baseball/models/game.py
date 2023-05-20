from uuid import uuid4
from typing import Tuple
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
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
    regulation_innings = models.PositiveSmallIntegerField(default=9, validators=[MinValueValidator(3)])
    rules = models.JSONField(default=dict, blank=True, null=True)

    # related models
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name='schedule', null=True)

    def __str__(self) -> str:
        if self.teams.count() == 2:
            return f'{self.away_team.team} at {self.home_team.team} : {self.date}'
        return f'Game at {self.date}'
    
    @property
    def home_team(self) -> CompetitionTeam:
        try:
            return self.teams.get(is_home_team=True).competition_team
        except Exception:
            return None
    
    @property
    def away_team(self) -> CompetitionTeam:
        try:
            return self.teams.get(is_home_team=False).competition_team
        except Exception:
            return None
    
    def add_team(self, competition_team: CompetitionTeam, is_home_team: bool) -> Tuple[str, bool]:
        """Add a team to the current game. 
        
        Returns false if game is full (already 2 teams), team is invalid(there is
        already a home/away team and you want the team to be home/away), or if the
        team has already been added to the game.
        """
        if self.teams.count() == 0:
            self.teams.create(competition_team=competition_team, is_home_team=is_home_team)
            return f'Successfully added CompetitionTeam \'{competition_team.id}\'.', True
        if self.teams.count() < 2:
            try:
                self.teams.get(competition_team=competition_team)
                return f'CompetitionTeam \'{competition_team.id}\' is already added to this game.', False
            except Exception:
                if is_home_team and self.home_team != None:
                    return 'There is already a home team in this game.', False
                if not is_home_team and self.away_team != None:
                    return 'There is already an away team in this game.', False
                self.teams.create(competition_team=competition_team, game=self, is_home_team=is_home_team)
                return f'Successfully added CompetitionTeam \'{competition_team.id}\'.', True
        return 'There are already 2 teams registered for this game.', False
    
    def get_opposing_team(self, competition_team: CompetitionTeam) -> CompetitionTeam | None:
        """Get the opposing team for the given team.
        """
        try:
            return self.teams.exclude(competition_team=competition_team).first().competition_team
        except Exception:
            return None
        
    def save(self, keep_deleted=False, **kwargs):
        self.full_clean()
        return super().save(keep_deleted, **kwargs)

def limit_teams(game_id: str):
    if Game.objects.filter(id=game_id).count() >= 2:
        raise ValidationError('No more than 2 teams can play in a game')