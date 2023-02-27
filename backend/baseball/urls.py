from django.urls import path

from baseball.views.competition_details import CompetitionDetails
from baseball.views.competition_list import CompetitionList
from baseball.views.coach_details import CoachDetails
from baseball.views.coach_list import CoachList
from baseball.views.player_details import PlayerDetails
from baseball.views.player_list import PlayerList
from baseball.views.organization_list import OrganizationList
from baseball.views.organization_details import OrganizationDetails

urlpatterns = [
    path('organizations/', OrganizationList.as_view()),
    path('organizations/<uuid:organization_id>/', OrganizationDetails.as_view()),
    path('competitions/', CompetitionList.as_view()),
    path('competitions/<uuid:competition_id>/', CompetitionDetails.as_view()),
    path('coaches/', CoachList.as_view()),
    path('coaches/<uuid:coach_id>/', CoachDetails.as_view()),
    path('players/', PlayerList.as_view()),
    path('players/<uuid:player_id>/', PlayerDetails.as_view()),
]
