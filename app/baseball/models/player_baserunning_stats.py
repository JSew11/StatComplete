from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

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
    picked_off_first = models.PositiveIntegerField(default=0)
    pickoff_attempts_first = models.PositiveIntegerField(default=0)
    # second base stats
    picked_off_second = models.PositiveIntegerField(default=0)
    pickoff_attempts_second = models.PositiveIntegerField(default=0)
    steals_second = models.PositiveIntegerField(default=0)
    caught_stealing_second = models.PositiveIntegerField(default=0)
    advanced_to_second = models.PositiveIntegerField(default=0)
    thrown_out_at_second = models.PositiveIntegerField(default=0)
    # third base stats
    picked_off_third = models.PositiveIntegerField(default=0)
    pickoff_attempts_third = models.PositiveIntegerField(default=0)
    advanced_to_third = models.PositiveIntegerField(default=0)
    thrown_out_at_third = models.PositiveIntegerField(default=0)
    steals_third= models.PositiveIntegerField(default=0)
    caught_stealing_third = models.PositiveIntegerField(default=0)
    # home plate stats
    runs_scored = models.PositiveIntegerField(default=0)
    thrown_out_at_home = models.PositiveIntegerField(default=0)
    steals_home = models.PositiveIntegerField(default=0)
    caught_stealing_home = models.PositiveIntegerField(default=0)

    # standard accumulated stats (less specific/more commonly used totals)
    @property
    def picked_off(self):
        return self.picked_off_first + self.picked_off_second + self.picked_off_third
    
    @property
    def pickoff_attempts(self):
        return self.pickoff_attempts_first + self.pickoff_attempts_second + self.pickoff_attempts_third
    
    @property
    def steals(self):
        return self.steals_second + self.steals_third + self.steals_home
    
    @property
    def caught_stealing(self):
        return self.caught_stealing_second + self.caught_stealing_third + self.caught_stealing_home
    
    @property
    def bases_advanced(self):
        return self.advanced_to_second + self.advanced_to_third + self.runs_scored
    
    @property
    def thrown_out(self):
        return self.thrown_out_at_second + self.thrown_out_at_third + self.thrown_out_at_home