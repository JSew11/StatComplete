from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .competition_coach import CompetitionCoach
from .competition_team import CompetitionTeam

class TeamCoach (SafeDeleteModel):
    """Model for a baseball coach's stats as a part of a specific team.

    Tracks the coach's record and time as a part of the associated team. 
    Includes the related competition coach, and competition team.
    """

    class CoachRole (models.IntegerChoices):
        """Choices for the different coaching roles as a part of a team.
        """
        COACH = 0, 'Coach'
        MANAGER = 1, 'Manager'
        ASSISTANT = 2, 'Assistant Coach'

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
    record = models.JSONField(default=dict, blank=True, null=True)
    role = models.PositiveSmallIntegerField(
        choices=CoachRole.choices,
        default=CoachRole.COACH
    )
    joined_team = models.DateField(blank=True, null=True)
    left_team = models.DateField(blank=True, null=True)

    # related models
    competition_coach = models.ForeignKey(CompetitionCoach, on_delete=models.SET_NULL, null=True, related_name='stats_by_team')
    competition_team = models.ForeignKey(CompetitionTeam, on_delete=models.SET_NULL, null=True, related_name='coach_stats')