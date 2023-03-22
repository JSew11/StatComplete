from django.contrib import admin

from .models.coach import Coach
from .models.player import Player
from .models.competition import Competition
from .models.organization import Organization
from .models.team import Team
from .models.competition_team import CompetitionTeam
from .models.team_coach import TeamCoach
from .models.team_player import TeamPlayer
from .models.game import Game

# Register your models here.
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Competition)
admin.site.register(Organization)
admin.site.register(Team)
admin.site.register(CompetitionTeam)
admin.site.register(Game)