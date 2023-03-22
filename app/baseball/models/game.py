from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from ..models.competition import Competition

class Game (SafeDeleteModel):
    """Model for a baseball game.
    
    Includes the game details (start time, venue, status, rules) and associated
    competition.
    """

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    class GameStatus (models.IntegerChoices):
        """Choices for the different statuses for a game.
        """
        SCHEDULED = 0, 'Scheduled'
        IN_PROGRESS = 1, 'In Progress'
        FINISHED = 2, 'Finished'
    
    class Meta:
        ordering = ['created']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
    
    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # game info
    date = models.DateTimeField(blank=True, null=True)
    venue = models.JSONField(default=dict)
    status = models.PositiveSmallIntegerField(
        choices=GameStatus.choices,
        default=GameStatus.SCHEDULED
    )
    rules = models.JSONField(default=dict)

    # related models
    competition = models.ForeignKey(Competition, on_delete=models.SET_NULL, related_name='schedule', null=True)

def limit_teams(game_id: str):
    if Game.objects.filter(id=game_id).count() >= 2:
        raise ValidationError('No more than 2 teams can play in a game')