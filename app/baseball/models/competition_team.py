from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from ..models.team import Team
from ..models.competition import Competition

class CompetitionTeam (SafeDeleteModel):
    """Model for a team participating in a competition.

    Includes the associated team and competition. Also includes stats for players and 
    coaches on the team (team total and by game).
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Competition Team'
        verbose_name_plural = 'Competition Teams'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    record = models.JSONField(default=dict)

    # related models
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='competition_teams', null=True)
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name='teams', null=True)

    def __str__(self) -> str:
        return f'{self.competition} - {self.team}'

def validate_team_jersey_number (jersey_number: int) -> bool:
    """Validator function for a team's jersey numbers as a part of a competition team.
    """
    # TODO: write this to check if a team/competition requires unique jersey numbers and
    #   validate if so
    return True