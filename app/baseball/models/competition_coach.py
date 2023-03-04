from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .coach import Coach
from .competition import Competition

class CompetitionCoach (SafeDeleteModel): 
    """Model for a baseball coach's stats for a specific competition.

    Includes the related coach and competition, as well as their stats for each
    team they coached as a part of that competition.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Coach Stats (Competition)'
        verbose_name_plural = 'Coach Stats (Competition)'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # related models
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='stats_by_competition')
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name='coaches', null=True)