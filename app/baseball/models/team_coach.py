from datetime import datetime
from typing import Any
from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .coach import Coach
from .competition_team import CompetitionTeam, validate_team_jersey_number
from .choices.coach_role import CoachRole

class TeamCoachManager (models.Manager):
    """Manager for team coach models.
    """
    def create(self, **kwargs: Any) -> Any:
        """Overridden create method"""
        team_coach: TeamCoach = super().create(**kwargs)
        team_coach.joined_team = datetime.now()
        team_coach.active = True
        return team_coach

class TeamCoach (SafeDeleteModel):
    """Model for a baseball coach's stats as a part of a specific team.

    Tracks the coach's record and time as a part of the associated team. 
    Includes the related competition coach, and competition team.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Coach Stats (Team)'
        verbose_name_plural = 'Coach Stats (Team)'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # team-specific info
    jersey_number = models.PositiveSmallIntegerField(null=True, validators=[validate_team_jersey_number])
    record = models.JSONField(default=dict, blank=True, null=True)
    role = models.PositiveSmallIntegerField(
        choices=CoachRole.choices,
        default=CoachRole.COACH
    )
    joined_team = models.DateTimeField(blank=True, null=True)
    left_team = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)

    # related models
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, related_name='stats_by_team')
    competition_team = models.ForeignKey(CompetitionTeam, on_delete=models.SET_NULL, null=True, related_name='coaching_staff')

    def __str__(self) -> str:
        string = str(self.coach)
        if self.jersey_number:
            string += f' #{self.jersey_number}'
        return string