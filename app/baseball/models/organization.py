from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class Organization (SafeDeleteModel):
    """Model for an organization.
    
    Includes the name, location, etc. Organizations can host competitions and create/
    manage teams.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE


    class Meta:
        ordering = ['created']
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # organization info
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name