from django.urls import path

from .views.competition_details import CompetitionDetails
from .views.competition_list import CompetitionList
from .views.coach_details import CoachDetails
from .views.coach_list import CoachList
from .views.player_details import PlayerDetails
from .views.player_list import PlayerList
from .views.organization_list import OrganizationList
from .views.organization_details import OrganizationDetails
from .views.team_list import TeamList

urlpatterns = [
    path('organizations/', OrganizationList.as_view()),
    path('organizations/<uuid:organization_id>/', OrganizationDetails.as_view()),
    path('competitions/', CompetitionList.as_view()),
    path('competitions/<uuid:competition_id>/', CompetitionDetails.as_view()),
    path('coaches/', CoachList.as_view()),
    path('coaches/<uuid:coach_id>/', CoachDetails.as_view()),
    path('players/', PlayerList.as_view()),
    path('players/<uuid:player_id>/', PlayerDetails.as_view()),
    path('teams/', TeamList.as_view()),
]
