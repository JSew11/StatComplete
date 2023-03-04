from django.urls import path

from ..views.player_details import PlayerDetails
from ..views.player_list import PlayerList

urlpatterns = [
    path('', PlayerList.as_view()),
    path('<uuid:player_id>/', PlayerDetails.as_view()),
]