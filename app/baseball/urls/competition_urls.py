from django.urls import path

from ..views.competition_viewset import CompetitionViewSet

competition_list = CompetitionViewSet.as_view({
    'get': 'list'
})

competition_details = CompetitionViewSet.as_view({
    'get': 'retrieve'
})

competition_team_registration = CompetitionViewSet.as_view({
    'post': 'register_team',
    'delete': 'unregister_team'
})

urlpatterns = [
    path('', competition_list),
    path('<uuid:competition_id>/', competition_details),
    path('<uuid:competition_id>/teams/<uuid:team_id>/', competition_team_registration),
]