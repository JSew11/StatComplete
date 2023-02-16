from django.contrib import admin

from .models.coach import Coach
from .models.coach_stats import CoachStats
from .models.player import Player

# Register your models here.
admin.site.register(Coach)
admin.site.register(CoachStats)
admin.site.register(Player)