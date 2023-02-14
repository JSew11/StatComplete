from uuid import uuid4
from django.db import models

class Coach (models.Model):
    """Model for a baseball coach.

    Includes generic info and record (total and by team).
    """
    PROTECTED_FIELDS = ['id', 'created_at', 'updated_at', 'stats_by_team']

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # coach info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Coach {self.first_name} {self.last_name}'
    