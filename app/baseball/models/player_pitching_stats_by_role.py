from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .choices.pitcher_role import PitcherRole
from .player_pitching_stats import PlayerPitchingStats

class PlayerPitchingStatsByRole(SafeDeleteModel):
    """Model for an individual player's pitching stats for a single role.
    
    Tracks counted pitching stats for a player pitching in a certain role.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Pitching Stats by Role'
        verbose_name_plural = 'Player Pitching Stats by Role'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # pitching stats model
    pitching_stats = models.ForeignKey(PlayerPitchingStats, on_delete=models.CASCADE, related_name='stats_by_role')

    # role
    role = models.PositiveSmallIntegerField(choices=PitcherRole.choices)

    # counted stats
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    no_decisions = models.PositiveIntegerField(default=0)
    games_pitched = models.PositiveIntegerField(default=0)
    games_finished = models.PositiveIntegerField(default=0)
    runs = models.PositiveIntegerField(default=0)
    earned_runs = models.PositiveIntegerField(default=0)
    balks = models.PositiveIntegerField(default=0)
    wild_pitches = models.PositiveIntegerField(default=0)
    outs_pitched = models.PositiveIntegerField(default=0) # pickoffs/caught stealings count here too (these are tracked in fielding)

    # matchup stats (tracked vs righties and vs lefties)
    strikes_thrown_vs_right = models.PositiveIntegerField(default=0)
    strikes_thrown_vs_left = models.PositiveIntegerField(default=0)
    balls_thrown_vs_right = models.PositiveIntegerField(default=0)
    balls_thrown_vs_left = models.PositiveIntegerField(default=0)

    batters_faced_vs_right = models.PositiveIntegerField(default=0)
    batters_faced_vs_left = models.PositiveIntegerField(default=0)

    singles_allowed_vs_right = models.PositiveIntegerField(default=0)
    singles_allowed_vs_left = models.PositiveIntegerField(default=0)
    doubles_allowed_vs_right = models.PositiveIntegerField(default=0)
    doubles_allowed_vs_left = models.PositiveIntegerField(default=0)
    triples_allowed_vs_right = models.PositiveIntegerField(default=0)
    triples_allowed_vs_left = models.PositiveIntegerField(default=0)
    home_runs_allowed_vs_right = models.PositiveIntegerField(default=0)
    home_runs_allowed_vs_left = models.PositiveIntegerField(default=0)

    walks_vs_right = models.PositiveIntegerField(default=0)
    walks_vs_left = models.PositiveIntegerField(default=0)
    intentional_walks_vs_right = models.PositiveIntegerField(default=0)
    intentional_walks_vs_left = models.PositiveIntegerField(default=0)

    hit_by_pitch_vs_right = models.PositiveIntegerField(default=0)
    hit_by_pitch_vs_left = models.PositiveIntegerField(default=0)

    strikeouts_swinging_vs_right = models.PositiveIntegerField(default=0)
    strikeouts_swinging_vs_left = models.PositiveIntegerField(default=0)
    strikeouts_looking_vs_right = models.PositiveIntegerField(default=0)
    strikeouts_looking_vs_left = models.PositiveIntegerField(default=0)

    ground_outs_forced_vs_right = models.PositiveIntegerField(default=0)
    ground_outs_forced_vs_left = models.PositiveIntegerField(default=0)
    line_outs_forced_vs_right = models.PositiveIntegerField(default=0)
    line_outs_forced_vs_left = models.PositiveIntegerField(default=0)
    fly_outs_forced_vs_right = models.PositiveIntegerField(default=0)
    fly_outs_forced_vs_left = models.PositiveIntegerField(default=0)
    pop_outs_forced_vs_right = models.PositiveIntegerField(default=0)
    pop_outs_forced_vs_left = models.PositiveIntegerField(default=0)
    
    def save(self, keep_deleted=False, **kwargs):
        self.full_clean()
        return super().save(keep_deleted, **kwargs)