from typing import Any
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .constants import RIGHT_HANDED_MATCHUP, LEFT_HANDED_MATCHUP

class PlayerBattingStats (SafeDeleteModel):
    """Model for an individual player's batting stats.
    
    Tracks standard counted batting stats, separated by lineup spot (location in
    the batting order).
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Batting Stats'
        verbose_name_plural = 'Player Batting Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # cumulative stat methods (total stat if no valid lineup spot)
    def games_started(self, lineup_spots: list = []) -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        return lineup_spot_stats.aggregate(models.Sum('games_started'))['games_started__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('games_started'))['games_started__sum'] or 0
    
    def games_pinch_hit(self, lineup_spots: list = []) -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        return lineup_spot_stats.aggregate(models.Sum('games_pinch_hit'))['games_pinch_hit__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('games_pinch_hit'))['games_pinch_hit__sum'] or 0
    
    def games_finished(self, lineup_spots: list = []) -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        return lineup_spot_stats.aggregate(models.Sum('games_finished'))['games_finished__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('games_finished'))['games_finished__sum'] or 0
    
    def complete_games(self, lineup_spots: list = []) -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        return lineup_spot_stats.aggregate(models.Sum('complete_games'))['complete_games__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('complete_games'))['complete_games__sum'] or 0

    # cumulative matchup stat methods (total if no valid roles and no valid matchup)
    def singles(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('singles_vs_right'))['singles_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('singles_vs_right'))['singles_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('singles_vs_left'))['singles_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('singles_vs_left'))['singles_vs_left__sum'] or 0
        singles_vs_right = lineup_spot_stats.aggregate(models.Sum('singles_vs_right'))['singles_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('singles_vs_right'))['singles_vs_right__sum'] or 0
        singles_vs_left = lineup_spot_stats.aggregate(models.Sum('singles_vs_left'))['singles_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('singles_vs_left'))['singles_vs_left__sum'] or 0
        return singles_vs_right + singles_vs_left

    def doubles(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('doubles_vs_right'))['doubles_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('doubles_vs_right'))['doubles_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('doubles_vs_left'))['doubles_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('doubles_vs_left'))['doubles_vs_left__sum'] or 0
        doubles_vs_right = lineup_spot_stats.aggregate(models.Sum('doubles_vs_right'))['doubles_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('doubles_vs_right'))['doubles_vs_right__sum'] or 0
        doubles_vs_left = lineup_spot_stats.aggregate(models.Sum('doubles_vs_left'))['doubles_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('doubles_vs_left'))['doubles_vs_left__sum'] or 0
        return doubles_vs_right + doubles_vs_left

    def triples(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('triples_vs_right'))['triples_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('triples_vs_right'))['triples_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('triples_vs_left'))['triples_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('triples_vs_left'))['triples_vs_left__sum'] or 0
        triples_vs_right = lineup_spot_stats.aggregate(models.Sum('triples_vs_right'))['triples_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('triples_vs_right'))['triples_vs_right__sum'] or 0
        triples_vs_left = lineup_spot_stats.aggregate(models.Sum('triples_vs_left'))['triples_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('triples_vs_left'))['triples_vs_left__sum'] or 0
        return triples_vs_right + triples_vs_left

    def home_runs(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('home_runs_vs_right'))['home_runs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('home_runs_vs_right'))['home_runs_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('home_runs_vs_left'))['home_runs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('home_runs_vs_left'))['home_runs_vs_left__sum'] or 0
        home_runs_vs_right = lineup_spot_stats.aggregate(models.Sum('home_runs_vs_right'))['home_runs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('home_runs_vs_right'))['home_runs_vs_right__sum'] or 0
        home_runs_vs_left = lineup_spot_stats.aggregate(models.Sum('home_runs_vs_left'))['home_runs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('home_runs_vs_left'))['home_runs_vs_left__sum'] or 0
        return home_runs_vs_right + home_runs_vs_left

    def runs_batted_in(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('runs_batted_in_vs_right'))['runs_batted_in_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('runs_batted_in_vs_right'))['runs_batted_in_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('runs_batted_in_vs_left'))['runs_batted_in_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('runs_batted_in_vs_left'))['runs_batted_in_vs_left__sum'] or 0
        runs_batted_in_vs_right = lineup_spot_stats.aggregate(models.Sum('runs_batted_in_vs_right'))['runs_batted_in_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('runs_batted_in_vs_right'))['runs_batted_in_vs_right__sum'] or 0
        runs_batted_in_vs_left = lineup_spot_stats.aggregate(models.Sum('runs_batted_in_vs_left'))['runs_batted_in_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('runs_batted_in_vs_left'))['runs_batted_in_vs_left__sum'] or 0
        return runs_batted_in_vs_right + runs_batted_in_vs_left

    def walks(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] or 0
        walks_vs_right = lineup_spot_stats.aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('walks_vs_right'))['walks_vs_right__sum'] or 0
        walks_vs_left = lineup_spot_stats.aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('walks_vs_left'))['walks_vs_left__sum'] or 0
        return walks_vs_right + walks_vs_left

    def intentional_walks(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] or 0
        intentional_walks_vs_right = lineup_spot_stats.aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('intentional_walks_vs_right'))['intentional_walks_vs_right__sum'] or 0
        intentional_walks_vs_left = lineup_spot_stats.aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('intentional_walks_vs_left'))['intentional_walks_vs_left__sum'] or 0
        return intentional_walks_vs_right + intentional_walks_vs_left

    def hit_by_pitch(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] or 0
        hit_by_pitch_vs_right = lineup_spot_stats.aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('hit_by_pitch_vs_right'))['hit_by_pitch_vs_right__sum'] or 0
        hit_by_pitch_vs_left = lineup_spot_stats.aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('hit_by_pitch_vs_left'))['hit_by_pitch_vs_left__sum'] or 0
        return hit_by_pitch_vs_right + hit_by_pitch_vs_left

    def sac_bunts(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('sac_bunts_vs_right'))['sac_bunts_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_bunts_vs_right'))['sac_bunts_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('sac_bunts_vs_left'))['sac_bunts_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_bunts_vs_left'))['sac_bunts_vs_left__sum'] or 0
        sac_bunts_vs_right = lineup_spot_stats.aggregate(models.Sum('sac_bunts_vs_right'))['sac_bunts_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_bunts_vs_right'))['sac_bunts_vs_right__sum'] or 0
        sac_bunts_vs_left = lineup_spot_stats.aggregate(models.Sum('sac_bunts_vs_left'))['sac_bunts_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_bunts_vs_left'))['sac_bunts_vs_left__sum'] or 0
        return sac_bunts_vs_right + sac_bunts_vs_left

    def sac_hits(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('sac_hits_vs_right'))['sac_hits_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_hits_vs_right'))['sac_hits_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('sac_hits_vs_left'))['sac_hits_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_hits_vs_left'))['sac_hits_vs_left__sum'] or 0
        sac_hits_vs_right = lineup_spot_stats.aggregate(models.Sum('sac_hits_vs_right'))['sac_hits_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_hits_vs_right'))['sac_hits_vs_right__sum'] or 0
        sac_hits_vs_left = lineup_spot_stats.aggregate(models.Sum('sac_hits_vs_left'))['sac_hits_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_hits_vs_left'))['sac_hits_vs_left__sum'] or 0
        return sac_hits_vs_right + sac_hits_vs_left

    def sac_flies(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('sac_flies_vs_right'))['sac_flies_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_flies_vs_right'))['sac_flies_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('sac_flies_vs_left'))['sac_flies_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_flies_vs_left'))['sac_flies_vs_left__sum'] or 0
        sac_flies_vs_right = lineup_spot_stats.aggregate(models.Sum('sac_flies_vs_right'))['sac_flies_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_flies_vs_right'))['sac_flies_vs_right__sum'] or 0
        sac_flies_vs_left = lineup_spot_stats.aggregate(models.Sum('sac_flies_vs_left'))['sac_flies_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('sac_flies_vs_left'))['sac_flies_vs_left__sum'] or 0
        return sac_flies_vs_right + sac_flies_vs_left

    def fielders_choice(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('fielders_choice_vs_right'))['fielders_choice_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fielders_choice_vs_right'))['fielders_choice_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('fielders_choice_vs_left'))['fielders_choice_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fielders_choice_vs_left'))['fielders_choice_vs_left__sum'] or 0
        fielders_choice_vs_right = lineup_spot_stats.aggregate(models.Sum('fielders_choice_vs_right'))['fielders_choice_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fielders_choice_vs_right'))['fielders_choice_vs_right__sum'] or 0
        fielders_choice_vs_left = lineup_spot_stats.aggregate(models.Sum('fielders_choice_vs_left'))['fielders_choice_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fielders_choice_vs_left'))['fielders_choice_vs_left__sum'] or 0
        return fielders_choice_vs_right + fielders_choice_vs_left

    def ground_outs(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('ground_outs_vs_right'))['ground_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('ground_outs_vs_right'))['ground_outs_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('ground_outs_vs_left'))['ground_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('ground_outs_vs_left'))['ground_outs_vs_left__sum'] or 0
        ground_outs_vs_right = lineup_spot_stats.aggregate(models.Sum('ground_outs_vs_right'))['ground_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('ground_outs_vs_right'))['ground_outs_vs_right__sum'] or 0
        ground_outs_vs_left = lineup_spot_stats.aggregate(models.Sum('ground_outs_vs_left'))['ground_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('ground_outs_vs_left'))['ground_outs_vs_left__sum'] or 0
        return ground_outs_vs_right + ground_outs_vs_left

    def line_outs(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('line_outs_vs_right'))['line_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('line_outs_vs_right'))['line_outs_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('line_outs_vs_left'))['line_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('line_outs_vs_left'))['line_outs_vs_left__sum'] or 0
        line_outs_vs_right = lineup_spot_stats.aggregate(models.Sum('line_outs_vs_right'))['line_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('line_outs_vs_right'))['line_outs_vs_right__sum'] or 0
        line_outs_vs_left = lineup_spot_stats.aggregate(models.Sum('line_outs_vs_left'))['line_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('line_outs_vs_left'))['line_outs_vs_left__sum'] or 0
        return line_outs_vs_right + line_outs_vs_left

    def fly_outs(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('fly_outs_vs_right'))['fly_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fly_outs_vs_right'))['fly_outs_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('fly_outs_vs_left'))['fly_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fly_outs_vs_left'))['fly_outs_vs_left__sum'] or 0
        fly_outs_vs_right = lineup_spot_stats.aggregate(models.Sum('fly_outs_vs_right'))['fly_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fly_outs_vs_right'))['fly_outs_vs_right__sum'] or 0
        fly_outs_vs_left = lineup_spot_stats.aggregate(models.Sum('fly_outs_vs_left'))['fly_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('fly_outs_vs_left'))['fly_outs_vs_left__sum'] or 0
        return fly_outs_vs_right + fly_outs_vs_left

    def pop_outs(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('pop_outs_vs_right'))['pop_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('pop_outs_vs_right'))['pop_outs_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('pop_outs_vs_left'))['pop_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('pop_outs_vs_left'))['pop_outs_vs_left__sum'] or 0
        pop_outs_vs_right = lineup_spot_stats.aggregate(models.Sum('pop_outs_vs_right'))['pop_outs_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('pop_outs_vs_right'))['pop_outs_vs_right__sum'] or 0
        pop_outs_vs_left = lineup_spot_stats.aggregate(models.Sum('pop_outs_vs_left'))['pop_outs_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('pop_outs_vs_left'))['pop_outs_vs_left__sum'] or 0
        return pop_outs_vs_right + pop_outs_vs_left

    def strikeouts_swinging(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] or 0
        strikeouts_swinging_vs_right = lineup_spot_stats.aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_swinging_vs_right'))['strikeouts_swinging_vs_right__sum'] or 0
        strikeouts_swinging_vs_left = lineup_spot_stats.aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_swinging_vs_left'))['strikeouts_swinging_vs_left__sum'] or 0
        return strikeouts_swinging_vs_right + strikeouts_swinging_vs_left

    def strikeouts_looking(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] or 0
        strikeouts_looking_vs_right = lineup_spot_stats.aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_looking_vs_right'))['strikeouts_looking_vs_right__sum'] or 0
        strikeouts_looking_vs_left = lineup_spot_stats.aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('strikeouts_looking_vs_left'))['strikeouts_looking_vs_left__sum'] or 0
        return strikeouts_looking_vs_right + strikeouts_looking_vs_left

    def double_plays(self, lineup_spots: list = [], matchup: str = '') -> int:
        lineup_spot_stats = self.stats_by_lineup_spot.filter(lineup_spot__in=lineup_spots)
        if matchup == RIGHT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('double_plays_vs_right'))['double_plays_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('double_plays_vs_right'))['double_plays_vs_right__sum'] or 0
        if matchup == LEFT_HANDED_MATCHUP:
            return lineup_spot_stats.aggregate(models.Sum('double_plays_vs_left'))['double_plays_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('double_plays_vs_left'))['double_plays_vs_left__sum'] or 0
        double_plays_vs_right = lineup_spot_stats.aggregate(models.Sum('double_plays_vs_right'))['double_plays_vs_right__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('double_plays_vs_right'))['double_plays_vs_right__sum'] or 0
        double_plays_vs_left = lineup_spot_stats.aggregate(models.Sum('double_plays_vs_left'))['double_plays_vs_left__sum'] if lineup_spot_stats else self.stats_by_lineup_spot.all().aggregate(models.Sum('double_plays_vs_left'))['double_plays_vs_left__sum'] or 0
        return double_plays_vs_right + double_plays_vs_left

    def update_stats_by_lineup_spot(self, lineup_spot: int, stats: dict) -> bool:
        """Update the player's batting stats for a specific lineup spot by adding
        the given value to the current stat value.
        """
        try:
            batting_stats_by_lineup_spot, _ = self.stats_by_lineup_spot.get_or_create(lineup_spot=lineup_spot)
            for name, stat in stats.items():
                try :
                    prev_val = getattr(batting_stats_by_lineup_spot, name)
                    setattr(batting_stats_by_lineup_spot, name, (prev_val+stat))
                except Exception:
                    continue
            batting_stats_by_lineup_spot.save()
            return True
        except ValidationError:
            return False