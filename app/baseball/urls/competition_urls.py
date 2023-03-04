from django.urls import path

from ..views.competition_details import CompetitionDetails
from ..views.competition_list import CompetitionList
from ..views.coach_competition_stats_list import CoachCompetitionStatsList

urlpatterns = [
    path('', CompetitionList.as_view()),
    path('<uuid:competition_id>/', CompetitionDetails.as_view()),
    path('<uuid:competition_id>/coaches/', CoachCompetitionStatsList.as_view()),
]