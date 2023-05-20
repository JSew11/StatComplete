from django.urls import path

from ..views.competition_viewset import CompetitionViewSet

competition_list = CompetitionViewSet.as_view({
    'get': 'list',
})

competition_details = CompetitionViewSet.as_view({
    'get': 'retrieve',
})

list_competition_teams = CompetitionViewSet.as_view({
    'get': 'list_teams',
})

manage_competition_teams = CompetitionViewSet.as_view({
    'post': 'register_team',
    'get': 'retrieve_team',
    'patch': 'update_team_record',
    'delete': 'unregister_team',
})

manage_competition_team_coaches = CompetitionViewSet.as_view({
    'post': 'create_team_coach',
    'patch': 'partial_update_team_coach',
    'delete': 'delete_team_coach',
})

manage_competition_team_players = CompetitionViewSet.as_view({
    'post': 'create_team_player',
    'put': 'update_player_stats',
})

list_competition_games = CompetitionViewSet.as_view({
    'post': 'create_game',
})

urlpatterns = [
    path('', competition_list),
    path('<uuid:competition_id>/', competition_details),
    path('<uuid:competition_id>/teams/', list_competition_teams),
    path('<uuid:competition_id>/teams/<uuid:team_id>/', manage_competition_teams),
    path('<uuid:competition_id>/teams/<uuid:team_id>/coaches/<uuid:coach_id>/', manage_competition_team_coaches),
    path('<uuid:competition_id>/teams/<uuid:team_id>/players/<uuid:player_id>/', manage_competition_team_players),
    path('<uuid:competition_id>/games/', list_competition_games)
]