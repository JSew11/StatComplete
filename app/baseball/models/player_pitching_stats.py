from typing import Any
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .constants import RIGHT_HANDED_MATCHUP, LEFT_HANDED_MATCHUP

class PlayerPitchingStats(SafeDeleteModel):
    """Model for an individual player's pitching stats.
    
    Tracks standard counted pitching stats for a player, separated by role.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Pitching Stats'
        verbose_name_plural = 'Player Pitching Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # counted stats (cannot be tracked by role)
    complete_games = models.PositiveIntegerField(default=0)
    shutouts = models.PositiveIntegerField(default=0)
    holds = models.PositiveIntegerField(default=0)
    saves = models.PositiveIntegerField(default=0)
    save_opportunities = models.PositiveIntegerField(default=0)

    @property
    def games_started(self):
        return self.stats_by_role.filter(role=0).first().games_pitched
    
    # cumulative stat methods (total stat if no valid roles)
    def wins(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('wins'))['wins__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('wins'))['wins__sum'] or 0

    def losses(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('losses'))['losses__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('losses'))['losses__sum'] or 0
    
    def no_decisions(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('no_decisions'))['no_decisions__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('no_decisions'))['no_decisions__sum'] or 0
    
    def games_pitched(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('games_pitched'))['games_pitched__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('games_pitched'))['games_pitched__sum'] or 0
    
    def games_finished(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('games_finished'))['games_finished__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('games_finished'))['games_finished__sum'] or 0

    def runs(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('runs'))['runs__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('runs'))['runs__sum'] or 0

    def earned_runs(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('earned_runs'))['earned_runs__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('earned_runs'))['earned_runs__sum'] or 0

    def balks(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('balks'))['balks__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('balks'))['balks__sum'] or 0

    def wild_pitches(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('wild_pitches'))['wild_pitches__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('wild_pitches'))['wild_pitches__sum'] or 0

    def outs_pitched(self, roles: list = []) -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        return role_stats.aggregate(models.Sum('outs_pitched'))['outs_pitched__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('outs_pitched'))['outs_pitched__sum'] or 0

    # cumulative matchup stat methods (total if no valid roles and no valid matchup)
    def strikes_thrown(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('strikes_thrown_vs_right'))['strikes_thrown_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikes_thrown_vs_right'))['strikes_thrown_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('strikes_thrown_vs_left'))['strikes_thrown_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikes_thrown_vs_left'))['strikes_thrown_vs_left__sum'] or 0
        strikes_thrown_vs_right = role_stats.aggregate(models.Sum('strikes_thrown_vs_right'))['strikes_thrown_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikes_thrown_vs_right'))['strikes_thrown_vs_right__sum'] or 0
        strikes_thrown_vs_left = role_stats.aggregate(models.Sum('strikes_thrown_vs_left'))['strikes_thrown_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikes_thrown_vs_left'))['strikes_thrown_vs_left__sum'] or 0
        return strikes_thrown_vs_right + strikes_thrown_vs_left
    
    def balls_thrown(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('balls_thrown_vs_right'))['balls_thrown_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('balls_thrown_vs_right'))['balls_thrown_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('balls_thrown_vs_left'))['balls_thrown_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('balls_thrown_vs_left'))['balls_thrown_vs_left__sum'] or 0
        balls_thrown_vs_right = role_stats.aggregate(models.Sum('balls_thrown_vs_right'))['balls_thrown_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('balls_thrown_vs_right'))['balls_thrown_vs_right__sum'] or 0
        balls_thrown_vs_left = role_stats.aggregate(models.Sum('balls_thrown_vs_left'))['balls_thrown_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('balls_thrown_vs_left'))['balls_thrown_vs_left__sum'] or 0
        return balls_thrown_vs_right + balls_thrown_vs_left

    def batters_faced(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('batters_faced_vs_right'))['batters_faced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('batters_faced_vs_right'))['batters_faced_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('batters_faced_vs_left'))['batters_faced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('batters_faced_vs_left'))['batters_faced_vs_left__sum'] or 0
        batters_faced_vs_right = role_stats.aggregate(models.Sum('batters_faced_vs_right'))['batters_faced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('batters_faced_vs_right'))['batters_faced_vs_right__sum'] or 0
        batters_faced_vs_left = role_stats.aggregate(models.Sum('batters_faced_vs_left'))['batters_faced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('batters_faced_vs_left'))['batters_faced_vs_left__sum'] or 0
        return batters_faced_vs_right + batters_faced_vs_left
    
    def singles_allowed(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('singles_allowed_vs_right'))['singles_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('singles_allowed_vs_right'))['singles_allowed_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('singles_allowed_vs_left'))['singles_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('singles_allowed_vs_left'))['singles_allowed_vs_left__sum'] or 0
        singles_allowed_vs_right = role_stats.aggregate(models.Sum('singles_allowed_vs_right'))['singles_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('singles_allowed_vs_right'))['singles_allowed_vs_right__sum'] or 0
        singles_allowed_vs_left = role_stats.aggregate(models.Sum('singles_allowed_vs_left'))['singles_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('singles_allowed_vs_left'))['singles_allowed_vs_left__sum'] or 0
        return singles_allowed_vs_right + singles_allowed_vs_left
        
    def doubles_allowed(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('doubles_allowed_vs_right'))['doubles_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('doubles_allowed_vs_right'))['doubles_allowed_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('doubles_allowed_vs_left'))['doubles_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('doubles_allowed_vs_left'))['doubles_allowed_vs_left__sum'] or 0
        doubles_allowed_vs_right = role_stats.aggregate(models.Sum('doubles_allowed_vs_right'))['doubles_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('doubles_allowed_vs_right'))['doubles_allowed_vs_right__sum'] or 0
        doubles_allowed_vs_left = role_stats.aggregate(models.Sum('doubles_allowed_vs_left'))['doubles_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('doubles_allowed_vs_left'))['doubles_allowed_vs_left__sum'] or 0
        return doubles_allowed_vs_right + doubles_allowed_vs_left
        
    def triples_allowed(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('triples_allowed_vs_right'))['triples_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('triples_allowed_vs_right'))['triples_allowed_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('triples_allowed_vs_left'))['triples_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('triples_allowed_vs_left'))['triples_allowed_vs_left__sum'] or 0
        triples_allowed_vs_right = role_stats.aggregate(models.Sum('triples_allowed_vs_right'))['triples_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('triples_allowed_vs_right'))['triples_allowed_vs_right__sum'] or 0
        triples_allowed_vs_left = role_stats.aggregate(models.Sum('triples_allowed_vs_left'))['triples_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('triples_allowed_vs_left'))['triples_allowed_vs_left__sum'] or 0
        return triples_allowed_vs_right + triples_allowed_vs_left
        
    def home_runs_allowed(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('home_runs_allowed_vs_right'))['home_runs_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('home_runs_allowed_vs_right'))['home_runs_allowed_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('home_runs_allowed_vs_left'))['home_runs_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('home_runs_allowed_vs_left'))['home_runs_allowed_vs_left__sum'] or 0
        home_runs_allowed_vs_right = role_stats.aggregate(models.Sum('home_runs_allowed_vs_right'))['home_runs_allowed_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('home_runs_allowed_vs_right'))['home_runs_allowed_vs_right__sum'] or 0
        home_runs_allowed_vs_left = role_stats.aggregate(models.Sum('home_runs_allowed_vs_left'))['home_runs_allowed_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('home_runs_allowed_vs_left'))['home_runs_allowed_vs_left__sum'] or 0
        return home_runs_allowed_vs_right + home_runs_allowed_vs_left
        
    def walks(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] or 0
        walks_vs_right = role_stats.aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] or 0
        walks_vs_left = role_stats.aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] or 0
        return walks_vs_right + walks_vs_left
        
    def intentional_walks(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] or 0
        intentional_walks_vs_right = role_stats.aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] or 0
        intentional_walks_vs_left = role_stats.aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] or 0
        return intentional_walks_vs_right + intentional_walks_vs_left
        
    def hit_by_pitch(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] or 0
        hit_by_pitch_vs_right = role_stats.aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] or 0
        hit_by_pitch_vs_left = role_stats.aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] or 0
        return hit_by_pitch_vs_right + hit_by_pitch_vs_left
        
    def strikeouts_swinging(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] or 0
        strikeouts_swinging_vs_right = role_stats.aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] or 0
        strikeouts_swinging_vs_left = role_stats.aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] or 0
        return strikeouts_swinging_vs_right + strikeouts_swinging_vs_left
        
    def strikeouts_looking(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] or 0
        strikeouts_looking_vs_right = role_stats.aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] or 0
        strikeouts_looking_vs_left = role_stats.aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] or 0
        return strikeouts_looking_vs_right + strikeouts_looking_vs_left
        
    def ground_outs_forced(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('ground_outs_forced_vs_right'))['ground_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('ground_outs_forced_vs_right'))['ground_outs_forced_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('ground_outs_forced_vs_left'))['ground_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('ground_outs_forced_vs_left'))['ground_outs_forced_vs_left__sum'] or 0
        ground_outs_forced_vs_right = role_stats.aggregate(models.Sum('ground_outs_forced_vs_right'))['ground_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('ground_outs_forced_vs_right'))['ground_outs_forced_vs_right__sum'] or 0
        ground_outs_forced_vs_left = role_stats.aggregate(models.Sum('ground_outs_forced_vs_left'))['ground_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('ground_outs_forced_vs_left'))['ground_outs_forced_vs_left__sum'] or 0
        return ground_outs_forced_vs_right + ground_outs_forced_vs_left
        
    def line_outs_forced(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('line_outs_forced_vs_right'))['line_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('line_outs_forced_vs_right'))['line_outs_forced_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('line_outs_forced_vs_left'))['line_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('line_outs_forced_vs_left'))['line_outs_forced_vs_left__sum'] or 0
        line_outs_forced_vs_right = role_stats.aggregate(models.Sum('line_outs_forced_vs_right'))['line_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('line_outs_forced_vs_right'))['line_outs_forced_vs_right__sum'] or 0
        line_outs_forced_vs_left = role_stats.aggregate(models.Sum('line_outs_forced_vs_left'))['line_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('line_outs_forced_vs_left'))['line_outs_forced_vs_left__sum'] or 0
        return line_outs_forced_vs_right + line_outs_forced_vs_left
        
    def fly_outs_forced(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('fly_outs_forced_vs_right'))['fly_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('fly_outs_forced_vs_right'))['fly_outs_forced_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('fly_outs_forced_vs_left'))['fly_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('fly_outs_forced_vs_left'))['fly_outs_forced_vs_left__sum'] or 0
        fly_outs_forced_vs_right = role_stats.aggregate(models.Sum('fly_outs_forced_vs_right'))['fly_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('fly_outs_forced_vs_right'))['fly_outs_forced_vs_right__sum'] or 0
        fly_outs_forced_vs_left = role_stats.aggregate(models.Sum('fly_outs_forced_vs_left'))['fly_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('fly_outs_forced_vs_left'))['fly_outs_forced_vs_left__sum'] or 0
        return fly_outs_forced_vs_right + fly_outs_forced_vs_left
        
    def pop_outs_forced(self, roles: list = [], matchup: str = '') -> int:
        role_stats = self.stats_by_role.filter(role__in=roles)
        if matchup == RIGHT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('pop_outs_forced_vs_right'))['pop_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('pop_outs_forced_vs_right'))['pop_outs_forced_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return role_stats.aggregate(models.Sum('pop_outs_forced_vs_left'))['pop_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('pop_outs_forced_vs_left'))['pop_outs_forced_vs_left__sum'] or 0
        pop_outs_forced_vs_right = role_stats.aggregate(models.Sum('pop_outs_forced_vs_right'))['pop_outs_forced_vs_right__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('pop_outs_forced_vs_right'))['pop_outs_forced_vs_right__sum'] or 0
        pop_outs_forced_vs_left = role_stats.aggregate(models.Sum('pop_outs_forced_vs_left'))['pop_outs_forced_vs_left__sum'] if role_stats else self.stats_by_role.all().aggregate(models.Sum('pop_outs_forced_vs_left'))['pop_outs_forced_vs_left__sum'] or 0
        return pop_outs_forced_vs_right + pop_outs_forced_vs_left
    
    # calculated stat methods
    def save_percentage(self) -> float:
        return self.saves / self.save_opportunities
    
    def win_percentage(self, roles: list = []) -> float:
        return self.wins(roles=roles) / self.games_pitched(roles=roles)
    
    def earned_run_average(self, roles: list = []) -> float:
        return (self.earned_runs(roles=roles) / self.innings_pitched(roles=roles)) * self.team_player.competition_team.competition.innings_per_game

    def innings_pitched(self, roles: list = [], formatted: bool = False) -> float:
        if formatted:
            return float(self.outs_pitched(roles=roles) // 3) + ((self.outs_pitched(roles=roles) % 3) / 10)
        return self.outs_pitched(roles=roles) / 3
    
    def pitches_thrown(self, roles: list = [], matchup: str = '') -> int:
        return (self.strikes_thrown(roles=roles, matchup=matchup) + 
                self.balls_thrown(roles=roles, matchup=matchup) + 
                self.hit_by_pitch(roles=roles, matchup=matchup))
    
    def hits_allowed(self, roles: list = [], matchup: str = '') -> int:
        return (self.singles_allowed(roles=roles, matchup=matchup) +
                self.doubles_allowed(roles=roles, matchup=matchup) +
                self.triples_allowed(roles=roles, matchup=matchup) +
                self.home_runs_allowed(roles=roles, matchup=matchup))
    
    def strikeouts(self, roles: list = [], matchup: str = '') -> int:
        return (self.strikeouts_swinging(roles=roles, matchup=matchup) +
                self.strikeouts_looking(roles=roles, matchup=matchup))

    def update_stats_by_role(self, role: int, stats: dict) -> bool:
        """Update the player's pitching stats for a specific role by adding the
        given value to the current stat value.
        """
        try:
            pitching_stats_by_role, _ = self.stats_by_role.get_or_create(role=role)
            for name, stat in stats.items():
                try :
                    prev_val = getattr(pitching_stats_by_role, name)
                    setattr(pitching_stats_by_role, name, (prev_val+stat))
                except Exception:
                    continue
            pitching_stats_by_role.save()
            return True
        except ValidationError:
            return False
