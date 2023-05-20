from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class Coach (SafeDeleteModel):
    """Model for a baseball coach.

    Includes generic info and record (total and by team).
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # coach info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'Coach {self.first_name} {self.last_name}'
    
    def get_competition_stats(self, competition_id):
        """Get the CoachCompetitionStats object for a specific competition
        """
        competition_stats = self.stats_by_competition.filter(competition__id=competition_id)
        return competition_stats[0]