from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class Player (SafeDeleteModel):
    """Model for a baseball player.
    
    Includes generic info and stats (total and by team).
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE
    PROTECTED_FIELDS = ['id', 'created', 'updated', 'deleted', 'stats_by_competition']

    class Meta:
        ordering = ['created']
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # player info
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    draft_class = models.PositiveSmallIntegerField(blank=True, null=True)
    physicals = models.JSONField(default=dict)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
