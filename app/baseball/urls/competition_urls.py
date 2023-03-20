from django.urls import path

from ..views.competition_viewset import CompetitionViewSet

competition_list = CompetitionViewSet.as_view({
    'get': 'list'
})

competition_details = CompetitionViewSet.as_view({
    'get': 'retrieve'
})

manage_competition_teams = CompetitionViewSet.as_view({
    'post': 'register_team',
    'patch': 'update_team_record',
    'delete': 'unregister_team'
})

manage_competition_team_coaches = CompetitionViewSet.as_view({
    'post': 'create_team_coach',
    'delete': 'delete_team_coach'
})

urlpatterns = [
    path('', competition_list),
    path('<uuid:competition_id>/', competition_details),
    path('<uuid:competition_id>/teams/<uuid:team_id>/', manage_competition_teams),
    path('<uuid:competition_id>/teams/<uuid:team_id>/coaches/<uuid:coach_id>/', manage_competition_team_coaches),
]