from django.contrib import admin

from .models.coach import Coach
from .models.coach_competition_stats import CoachCompetitionStats
from .models.player import Player
from .models.player_stats import PlayerStats

# Register your models here.
admin.site.register(Coach)
admin.site.register(CoachCompetitionStats)
admin.site.register(Player)
admin.site.register(PlayerStats)