from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class Competition (SafeDeleteModel):
    """Model for a baseball competition.

    Includes the type (season, tournament, etc.), standings, schedule and
    start/end dates.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'