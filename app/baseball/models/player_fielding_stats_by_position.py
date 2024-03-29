from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .choices.fielding_position import FieldingPosition
from .player_fielding_stats import PlayerFieldingStats

class PlayerFieldingStatsByPosition (SafeDeleteModel):
    """Model for an individual player's fielding stats for a single position.
    
    Tracks counted fielding stats for a player playing a certain fielding position.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Fielding Stats by Position'
        verbose_name_plural = 'Player Fielding Stats by Position'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # fielding stats model
    fielding_stats = models.ForeignKey(PlayerFieldingStats, on_delete=models.CASCADE, related_name='stats_by_position')

    # position
    position = models.PositiveSmallIntegerField(choices=FieldingPosition.choices)

    # game tracking stats
    games_started = models.PositiveIntegerField(default=0)
    games_subbed_in = models.PositiveIntegerField(default=0)
    games_finished = models.PositiveIntegerField(default=0)
    complete_games = models.PositiveIntegerField(default=0)

    # counted stats
    putouts = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    fielding_errors = models.PositiveIntegerField(default=0)
    throwing_errors = models.PositiveIntegerField(default=0)
    outs_played = models.PositiveIntegerField(default=0)
    double_plays = models.PositiveIntegerField(default=0)

    # catcher/pitcher exclusive stats
    passed_balls = models.PositiveIntegerField(default=0)
    pickoffs_first_base = models.PositiveIntegerField(default=0)
    pickoff_attempts_first_base = models.PositiveIntegerField(default=0)
    pickoffs_second_base = models.PositiveIntegerField(default=0)
    pickoff_attempts_second_base = models.PositiveIntegerField(default=0)
    steals_against_second_base = models.PositiveIntegerField(default=0)
    caught_stealing_second_base = models.PositiveIntegerField(default=0)
    pickoffs_third_base = models.PositiveIntegerField(default=0)
    pickoff_attempts_third_base = models.PositiveIntegerField(default=0)
    steals_against_third_base = models.PositiveIntegerField(default=0)
    caught_stealing_third_base = models.PositiveIntegerField(default=0)
    steals_against_home_plate = models.PositiveIntegerField(default=0)
    caught_stealing_home_plate = models.PositiveIntegerField(default=0)

    def save(self, keep_deleted=False, **kwargs):
        self.full_clean()
        return super().save(keep_deleted, **kwargs)