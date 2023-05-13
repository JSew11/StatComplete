from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .constants import FIRST_BASE, SECOND_BASE, THIRD_BASE, HOME_PLATE

class PlayerBaserunningStats(SafeDeleteModel):
    """Model for an individual player's baserunning stats.
    
    Tracks baserunning stats for a player.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Baserunning Stats'
        verbose_name_plural = 'Player Baserunning Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # counted stats (more specific/less commonly used)
    games_pinch_run = models.PositiveIntegerField(default=0)
    # first base stats
    picked_off_first_base = models.PositiveIntegerField(default=0)
    pickoff_attempts_first_base = models.PositiveIntegerField(default=0)
    # second base stats
    picked_off_second_base = models.PositiveIntegerField(default=0)
    pickoff_attempts_second_base = models.PositiveIntegerField(default=0)
    steals_second_base = models.PositiveIntegerField(default=0)
    caught_stealing_second_base = models.PositiveIntegerField(default=0)
    advanced_to_second_base = models.PositiveIntegerField(default=0)
    thrown_out_at_second_base = models.PositiveIntegerField(default=0)
    # third base stats
    picked_off_third_base = models.PositiveIntegerField(default=0)
    pickoff_attempts_third_base = models.PositiveIntegerField(default=0)
    advanced_to_third_base = models.PositiveIntegerField(default=0)
    thrown_out_at_third_base = models.PositiveIntegerField(default=0)
    steals_third_base = models.PositiveIntegerField(default=0)
    caught_stealing_third_base = models.PositiveIntegerField(default=0)
    # home plate stats
    runs_scored = models.PositiveIntegerField(default=0)
    thrown_out_at_home_plate = models.PositiveIntegerField(default=0)
    steals_home_plate = models.PositiveIntegerField(default=0)
    caught_stealing_home_plate = models.PositiveIntegerField(default=0)

    # standard accumulated stats (less specific/more commonly used totals)
    def picked_off(self, base: str = '') -> int:
        if base == FIRST_BASE:
            return self.picked_off_first_base
        if base == SECOND_BASE:
            return self.picked_off_second_base
        if base == THIRD_BASE:
            return self.picked_off_third_base
        return self.picked_off_first_base + self.picked_off_second_base + self.picked_off_third_base
    
    def pickoff_attempts(self, base: str = '') -> int:
        if base == FIRST_BASE:
            return self.pickoff_attempts_first_base
        if base == SECOND_BASE:
            return self.pickoff_attempts_second_base
        if base == THIRD_BASE:
            return self.pickoff_attempts_third_base
        return self.pickoff_attempts_first_base + self.pickoff_attempts_second_base + self.pickoff_attempts_third_base
    
    def steals(self, base: str = '') -> int:
        if base == SECOND_BASE:
            return self.steals_second_base
        if base == THIRD_BASE:
            return self.steals_third_base
        if base == HOME_PLATE:
            return self.steals_home_plate
        return self.steals_second_base + self.steals_third_base + self.steals_home_plate
    
    def caught_stealing(self, base: str = '') -> int:
        if base == SECOND_BASE:
            return self.caught_stealing_second_base
        if base == THIRD_BASE:
            return self.caught_stealing_third_base
        if base == HOME_PLATE:
            return self.caught_stealing_home_plate
        return self.caught_stealing_second_base + self.caught_stealing_third_base + self.caught_stealing_home_plate
    
    def bases_advanced(self, base: str = '') -> int:
        if base == SECOND_BASE:
            return self.advanced_to_second_base
        if base == THIRD_BASE:
            return self.advanced_to_third_base
        if base == HOME_PLATE:
            return self.runs_scored
        return self.advanced_to_second_base + self.advanced_to_third_base + self.runs_scored
    
    def thrown_out(self, base: str = '') -> int:
        if base == SECOND_BASE:
            return self.thrown_out_at_second_base
        if base == THIRD_BASE:
            return self.thrown_out_at_third_base
        if base == HOME_PLATE:
            return self.thrown_out_at_home_plate
        return self.thrown_out_at_second_base + self.thrown_out_at_third_base + self.thrown_out_at_home_plate