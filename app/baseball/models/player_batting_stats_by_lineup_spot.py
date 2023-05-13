from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .player_batting_stats import PlayerBattingStats

class PlayerBattingStatsByLineupSpot(SafeDeleteModel):
    """Model for an individual player's batting stats for a single spot in the
    lineup.
    
    Tracks counted batting stats for a player batting in a certain lineup spot.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Batting Stats by Lineup Spot'
        verbose_name_plural = 'Player Batting Stats by Lineup Spot'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # batting stats model
    batting_stats = models.ForeignKey(PlayerBattingStats, on_delete=models.CASCADE, related_name='stats_by_lineup_spot')

    # lineup spot
    lineup_spot = models.PositiveSmallIntegerField()

    # counted stats
    games_started = models.PositiveIntegerField(default=0)
    games_pinch_hit = models.PositiveIntegerField(default=0)
    games_finished = models.PositiveIntegerField(default=0)
    complete_games = models.PositiveIntegerField(default=0)

    # matchup stats (tracked vs righties and vs lefties)
    singles_vs_right = models.PositiveIntegerField(default=0)
    singles_vs_left = models.PositiveIntegerField(default=0)
    doubles_vs_right = models.PositiveIntegerField(default=0)
    doubles_vs_left = models.PositiveIntegerField(default=0)
    triples_vs_right = models.PositiveIntegerField(default=0)
    triples_vs_left = models.PositiveIntegerField(default=0)
    home_runs_vs_right = models.PositiveIntegerField(default=0)
    home_runs_vs_left = models.PositiveIntegerField(default=0)

    runs_batted_in_vs_right = models.PositiveIntegerField(default=0)
    runs_batted_in_vs_left = models.PositiveIntegerField(default=0)

    walks_vs_right = models.PositiveIntegerField(default=0)
    walks_vs_left = models.PositiveIntegerField(default=0)
    intentional_walks_vs_right = models.PositiveIntegerField(default=0)
    intentional_walks_vs_left = models.PositiveIntegerField(default=0)

    hit_by_pitch_vs_right = models.PositiveIntegerField(default=0)
    hit_by_pitch_vs_left = models.PositiveIntegerField(default=0)
    
    sac_bunts_vs_right = models.PositiveIntegerField(default=0)
    sac_bunts_vs_left = models.PositiveIntegerField(default=0)
    sac_hits_vs_right = models.PositiveIntegerField(default=0)
    sac_hits_vs_left = models.PositiveIntegerField(default=0)
    sac_flies_vs_right = models.PositiveIntegerField(default=0)
    sac_flies_vs_left = models.PositiveIntegerField(default=0)

    fielders_choice_vs_right = models.PositiveIntegerField(default=0)
    fielders_choice_vs_left = models.PositiveIntegerField(default=0)

    ground_outs_vs_right = models.PositiveIntegerField(default=0)
    ground_outs_vs_left = models.PositiveIntegerField(default=0)
    line_outs_vs_right = models.PositiveIntegerField(default=0)
    line_outs_vs_left = models.PositiveIntegerField(default=0)
    fly_outs_vs_right = models.PositiveIntegerField(default=0)
    fly_outs_vs_left = models.PositiveIntegerField(default=0)
    pop_outs_vs_right = models.PositiveIntegerField(default=0)
    pop_outs_vs_left = models.PositiveIntegerField(default=0)

    strikeouts_swinging_vs_right = models.PositiveIntegerField(default=0)
    strikeouts_swinging_vs_left = models.PositiveIntegerField(default=0)
    strikeouts_looking_vs_right = models.PositiveIntegerField(default=0)
    strikeouts_looking_vs_left = models.PositiveIntegerField(default=0)

    double_plays_vs_right = models.PositiveIntegerField(default=0)
    double_plays_vs_left = models.PositiveIntegerField(default=0)

    def save(self, keep_deleted=False, **kwargs):
        self.full_clean()
        return super().save(keep_deleted, **kwargs)