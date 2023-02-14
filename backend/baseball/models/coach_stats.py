from uuid import uuid4
from django.db import models

from .coach import Coach

class CoachStats (models.Model): 
    """Model for a baseball coach's stats.

    Includes the related coach and team, as well as a json object storing 
    stat data.
    """
    PROTECTED_FIELDS = ['id', 'created_at', 'updated_at']

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Coach Stats'
        verbose_name_plural = 'Coach Stats'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # related models
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='stats_by_team')

    # stats/team-specific info
    jersey_number = models.PositiveSmallIntegerField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    stats = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.coach + ' #' + self.jersey_number if self.jersey_number else self.coach