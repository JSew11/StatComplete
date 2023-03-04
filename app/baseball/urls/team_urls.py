from django.urls import path

from ..views.team_list import TeamList
from ..views.team_details import TeamDetails

urlpatterns = [
    path('', TeamList.as_view()),
    path('<uuid:team_id>/', TeamDetails.as_view()),
]