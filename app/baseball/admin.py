from django.contrib import admin

from .models.coach import Coach
from .models.coach_competition_stats import CoachCompetitionStats
from .models.player import Player
from .models.player_competition_stats import PlayerCompetitionStats
from .models.competition import Competition
from .models.organization import Organization
from .models.team import Team
from .models.competition_team import CompetitionTeam

# Register your models here.
admin.site.register(Coach)
admin.site.register(CoachCompetitionStats)
admin.site.register(Player)
admin.site.register(PlayerCompetitionStats)
admin.site.register(Competition)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(CompetitionTeam)