from django.contrib import admin

from .models.organization import Organization
from .models.team import Team
from .models.competition import Competition
from .models.competition_team import CompetitionTeam
from .models.coach import Coach
from .models.team_coach import TeamCoach
from .models.player import Player
from .models.team_player import TeamPlayer
from .models.player_baserunning_stats import PlayerBaserunningStats
from .models.player_pitching_stats import PlayerPitchingStats
from .models.player_pitching_stats_by_role import PlayerPitchingStatsByRole
from .models.game import Game
from .models.team_box_score import TeamBoxScore

# Register your models here.
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Competition)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(CompetitionTeam)
admin.site.register(Game)