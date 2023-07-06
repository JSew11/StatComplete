from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from core.models.organization import Organization
from .choices.competition_type import CompetitionType

class Competition (SafeDeleteModel):
    """Model for a baseball competition.

    Includes the type (season, tournament, etc.), standings and
    start/end dates.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # competition info
    name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(
        choices=CompetitionType.choices, 
        default=CompetitionType.SEASON
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    game_rules = models.JSONField(default=dict)

    # common rules
    innings_per_game = models.PositiveSmallIntegerField(default=9)

    # related models
    organizer = models.ForeignKey(Organization, on_delete=models.SET_NULL, related_name='competitions', null=True)

    def __str__(self) -> str:
        return self.name