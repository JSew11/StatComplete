from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from ..models.organization import Organization

class Competition (SafeDeleteModel):
    """Model for a baseball competition.

    Includes the type (season, tournament, etc.), standings, schedule and
    start/end dates.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class CompetitionType (models.IntegerChoices):
        """Choices for the different types of competitions.
        """
        SEASON = 1, 'Season'
        TOURNAMENT = 2, 'Tournament'

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