from django.urls import path

from ..views.competition_details import CompetitionDetails
from ..views.competition_list import CompetitionList
from ..views.competition_coach_details import CompetitionCoachDetails
from ..views.competition_coach_list import CompetitionCoachList

urlpatterns = [
    path('', CompetitionList.as_view()),
    path('<uuid:competition_id>/', CompetitionDetails.as_view()),
    path('<uuid:competition_id>/coaches/', CompetitionCoachList.as_view()),
    path('<uuid:competition_id>/coaches/<uuid:coach_id>/', CompetitionCoachDetails.as_view()),
]