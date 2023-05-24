from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from core.models.organization import Organization

class Team (SafeDeleteModel):
    """Model for a baseball team.
    
    Includes generic info and an Organization relationship.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        ordering = ['created']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # team info
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # related models
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, related_name='teams', null=True)

    def __str__(self) -> str:
        return f'{self.location} {self.name}'