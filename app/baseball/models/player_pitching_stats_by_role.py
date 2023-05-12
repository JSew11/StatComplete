from uuid import uuid4
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .player_pitching_stats import PlayerPitchingStats

class PlayerPitchingStatsByRole(SafeDeleteModel):
    """Model for an individual player's pitching stats for an individual role.
    
    Tracks counted pitching stats for a player pitching in a certain role.
    """

    class PitcherRole(models.IntegerChoices):
        """Choices for the different roles a pitcher can have.
        """
        STARTING_PITCHER = 0, 'SP'
        RELIEF_PITCHER = 1, 'RP'

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

    # matchup stats (tracked vs righties and vs lefties)
    strikes_thrown_vs_right = models.PositiveIntegerField(default=0)
    strikes_thrown_vs_left = models.PositiveIntegerField(default=0)
    balls_thrown_vs_right = models.PositiveIntegerField(default=0)
    balls_thrown_vs_left = models.PositiveIntegerField(default=0)

    righty_batters_faced = models.PositiveIntegerField(default=0)
    lefty_batters_faced = models.PositiveIntegerField(default=0)

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

    # combined stats (matchup vs right + matchup vs left)
    @property
    def strikes_thrown(self):
        return self.strikes_thrown_vs_right + self.strikes_thrown_vs_left
    
    @property
    def balls_thrown(self):
        return self.balls_thrown_vs_right + self.balls_thrown_vs_left

    @property
    def batters_faced(self):
        return self.righty_batters_faced + self.lefty_batters_faced
    
    @property
    def singles_allowed(self):
        return self.singles_allowed_vs_right + self.singles_allowed_vs_left
    
    @property
    def doubles_allowed(self):
        return self.doubles_allowed_vs_right + self.doubles_allowed_vs_left
    
    @property
    def triples_allowed(self):
        return self.triples_allowed_vs_right + self.triples_allowed_vs_left
    
    @property
    def home_runs_allowed(self):
        return self.home_runs_allowed_vs_right + self.home_runs_allowed_vs_left
    
    @property
    def walks(self):
        return self.walks_vs_right + self.walks_vs_left
    
    @property
    def intentional_walks(self):
        return self.intentional_walks_vs_right + self.intentional_walks_vs_left
    
    @property
    def hit_by_pitch(self):
        return self.hit_by_pitch_vs_right + self.hit_by_pitch_vs_left

    @property
    def strikeouts_swinging(self):
        return self.strikeouts_swinging_vs_right + self.strikeouts_swinging_vs_left
    
    @property
    def strikeouts_looking(self):
        return self.strikeouts_looking_vs_right + self.strikeouts_looking_vs_left

    @property
    def ground_outs_forced(self):
        return self.ground_outs_forced_vs_right + self.ground_outs_forced_vs_left
    
    @property
    def line_outs_forced(self):
        return self.line_outs_forced_vs_right + self.line_outs_forced_vs_left
    
    @property
    def fly_outs_forced(self):
        return self.fly_outs_forced_vs_right + self.fly_outs_forced_vs_left
    
    @property
    def pop_outs_forced(self):
        return self.pop_outs_forced_vs_right + self.pop_outs_forced_vs_left

    # other counted stats
    runs = models.PositiveIntegerField(default=0)
    earned_runs = models.PositiveIntegerField(default=0)
    balks = models.PositiveIntegerField(default=0)
    wild_pitches = models.PositiveIntegerField(default=0)
    outs_pitched = models.PositiveIntegerField(default=0) # pickoffs/caught stealings count here too (these are tracked in fielding)

    # cumulative stats
    @property
    def pitches_thrown(self):
        return self.strikes_thrown + self.balls_thrown
    
    @property
    def hits_allowed(self):
        return self.singles_allowed + self.doubles_allowed + self.triples_allowed + self.home_runs_allowed
    
    @property
    def strikeouts(self):
        return self.strikeouts_looking + self.strikeouts_swinging
