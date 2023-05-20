from typing import Any
from uuid import uuid4
from django.db import models
from django.core.exceptions import ValidationError
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

from .constants import FIRST_BASE, SECOND_BASE, THIRD_BASE, HOME_PLATE

class PlayerFieldingStats (SafeDeleteModel):
    """Model for an individual player's fielding stats.
    
    Tracks standard counted fielding stats, separated by position.
    """

    class Meta:
        ordering = ['created']
        verbose_name = 'Player Fielding Stats'
        verbose_name_plural = 'Player Fielding Stats'

    deleted_by_cascade = None # removes this default field from the db table
    _safedelete_policy = SOFT_DELETE_CASCADE

    # database info
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # cumulative stat methods (total stat if no valid position)
    def games_started(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('games_started'))['games_started__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('games_started'))['games_started__sum'] or 0

    def games_subbed_in(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('games_subbed_in'))['games_subbed_in__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('games_subbed_in'))['games_subbed_in__sum'] or 0

    def games_finished(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('games_finished'))['games_finished__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('games_finished'))['games_finished__sum'] or 0

    def complete_games(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('complete_games'))['complete_games__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('complete_games'))['complete_games__sum'] or 0

    def putouts(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('putouts'))['putouts__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('putouts'))['putouts__sum'] or 0

    def assists(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('assists'))['assists__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('assists'))['assists__sum'] or 0

    def fielding_errors(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('fielding_errors'))['fielding_errors__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('fielding_errors'))['fielding_errors__sum'] or 0

    def throwing_errors(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('throwing_errors'))['throwing_errors__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('throwing_errors'))['throwing_errors__sum'] or 0

    def outs_played(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('outs_played'))['outs_played__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('outs_played'))['outs_played__sum'] or 0

    def double_plays(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('double_plays'))['double_plays__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('double_plays'))['double_plays__sum'] or 0

    def passed_balls(self, positions: list = []) -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        return position_stats.aggregate(models.Sum('passed_balls'))['passed_balls__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('passed_balls'))['passed_balls__sum'] or 0
    
    # cumulative base stat methods (total if no valid position and no valid base)
    def pickoffs(self, positions: list = [], base: str = '') -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        if base == FIRST_BASE:
            return position_stats.aggregate(models.Sum('pickoffs_first_base'))['pickoffs_first_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoffs_first_base'))['pickoffs_first_base__sum'] or 0
        if base == SECOND_BASE:
            return position_stats.aggregate(models.Sum('pickoffs_second_base'))['pickoffs_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoffs_second_base'))['pickoffs_second_base__sum'] or 0
        if base == THIRD_BASE:
            return position_stats.aggregate(models.Sum('pickoffs_third_base'))['pickoffs_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoffs_third_base'))['pickoffs_third_base__sum'] or 0
        pickoffs_first_base = position_stats.aggregate(models.Sum('pickoffs_first_base'))['pickoffs_first_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoffs_first_base'))['pickoffs_first_base__sum'] or 0
        pickoffs_second_base = position_stats.aggregate(models.Sum('pickoffs_second_base'))['pickoffs_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoffs_second_base'))['pickoffs_second_base__sum'] or 0
        pickoffs_third_base = position_stats.aggregate(models.Sum('pickoffs_third_base'))['pickoffs_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoffs_third_base'))['pickoffs_third_base__sum'] or 0
        return pickoffs_first_base + pickoffs_second_base + pickoffs_third_base

    def pickoff_attempts(self, positions: list = [], base: str = '') -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        if base == FIRST_BASE:
            return position_stats.aggregate(models.Sum('pickoff_attempts_first_base'))['pickoff_attempts_first_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoff_attempts_first_base'))['pickoff_attempts_first_base__sum'] or 0
        if base == SECOND_BASE:
            return position_stats.aggregate(models.Sum('pickoff_attempts_second_base'))['pickoff_attempts_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoff_attempts_second_base'))['pickoff_attempts_second_base__sum'] or 0
        if base == THIRD_BASE:
            return position_stats.aggregate(models.Sum('pickoff_attempts_third_base'))['pickoff_attempts_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoff_attempts_third_base'))['pickoff_attempts_third_base__sum'] or 0
        pickoff_attempts_first_base = position_stats.aggregate(models.Sum('pickoff_attempts_first_base'))['pickoff_attempts_first_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoff_attempts_first_base'))['pickoff_attempts_first_base__sum'] or 0
        pickoff_attempts_second_base = position_stats.aggregate(models.Sum('pickoff_attempts_second_base'))['pickoff_attempts_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoff_attempts_second_base'))['pickoff_attempts_second_base__sum'] or 0
        pickoff_attempts_third_base = position_stats.aggregate(models.Sum('pickoff_attempts_third_base'))['pickoff_attempts_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('pickoff_attempts_third_base'))['pickoff_attempts_third_base__sum'] or 0
        return pickoff_attempts_first_base + pickoff_attempts_second_base + pickoff_attempts_third_base

    def steals_against(self, positions: list = [], base: str = '') -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        if base == SECOND_BASE:
            return position_stats.aggregate(models.Sum('steals_against_second_base'))['steals_against_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('steals_against_second_base'))['steals_against_second_base__sum'] or 0
        if base == THIRD_BASE:
            return position_stats.aggregate(models.Sum('steals_against_third_base'))['steals_against_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('steals_against_third_base'))['steals_against_third_base__sum'] or 0
        if base == HOME_PLATE:
            return position_stats.aggregate(models.Sum('steals_against_home_plate'))['steals_against_home_plate__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('steals_against_home_plate'))['steals_against_home_plate__sum'] or 0
        steals_against_second_base = position_stats.aggregate(models.Sum('steals_against_second_base'))['steals_against_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('steals_against_second_base'))['steals_against_second_base__sum'] or 0
        steals_against_third_base = position_stats.aggregate(models.Sum('steals_against_third_base'))['steals_against_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('steals_against_third_base'))['steals_against_third_base__sum'] or 0
        steals_against_home_plate = position_stats.aggregate(models.Sum('steals_against_home_plate'))['steals_against_home_plate__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('steals_against_home_plate'))['steals_against_home_plate__sum'] or 0
        return (steals_against_second_base + steals_against_third_base + steals_against_home_plate)

    def caught_stealing(self, positions: list = [], base: str = '') -> int:
        position_stats = self.stats_by_position.filter(position__in=positions)
        if base == SECOND_BASE:
            return position_stats.aggregate(models.Sum('caught_stealing_second_base'))['caught_stealing_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('caught_stealing_second_base'))['caught_stealing_second_base__sum'] or 0
        if base == THIRD_BASE:
            return position_stats.aggregate(models.Sum('caught_stealing_third_base'))['caught_stealing_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('caught_stealing_third_base'))['caught_stealing_third_base__sum'] or 0
        if base == HOME_PLATE:
            return position_stats.aggregate(models.Sum('caught_stealing_home_plate'))['caught_stealing_home_plate__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('caught_stealing_home_plate'))['caught_stealing_home_plate__sum'] or 0
        caught_stealing_second_base = position_stats.aggregate(models.Sum('caught_stealing_second_base'))['caught_stealing_second_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('caught_stealing_second_base'))['caught_stealing_second_base__sum'] or 0
        caught_stealing_third_base = position_stats.aggregate(models.Sum('caught_stealing_third_base'))['caught_stealing_third_base__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('caught_stealing_third_base'))['caught_stealing_third_base__sum'] or 0
        caught_stealing_home_plate = position_stats.aggregate(models.Sum('caught_stealing_home_plate'))['caught_stealing_home_plate__sum'] if position_stats else self.stats_by_position.all().aggregate(models.Sum('caught_stealing_home_plate'))['caught_stealing_home_plate__sum'] or 0
        return (caught_stealing_second_base + caught_stealing_third_base + caught_stealing_home_plate)

    def update_stats_by_position(self, position: int, stats: dict) -> bool:
        """Update the player's fielding stats for a specific position by adding the
        given value to the current stat value.
        """
        try:
            fielding_stats_by_position, _ = self.stats_by_position.get_or_create(position=position)
            for name, stat in stats.items():
                try :
                    prev_val = getattr(fielding_stats_by_position, name)
                    setattr(fielding_stats_by_position, name, (prev_val+stat))
                except Exception:
                    continue
            fielding_stats_by_position.save()
            return True
        except ValidationError:
            return False
