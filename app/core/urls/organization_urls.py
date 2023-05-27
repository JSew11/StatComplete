from django.urls import path

from ..views.organization_viewset import OrganizationViewSet
from ..views.organization_baseball_viewset import OrganizationBaseballCompetitionViewset, OrganizationBaseballTeamViewset

organization_list = OrganizationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

organization_details = OrganizationViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

organization_competition_list = OrganizationBaseballCompetitionViewset.as_view({
    'get': 'list',
    'post': 'create'
})

organization_competition_details = OrganizationBaseballCompetitionViewset.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

organization_team_list = OrganizationBaseballTeamViewset.as_view({
    'get': 'list',
    'post': 'create'
})

organization_team_details = OrganizationBaseballTeamViewset.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', organization_list),
    path('<uuid:organization_id>/', organization_details),
    path('<uuid:organization_id>/baseball/competitions/', organization_competition_list),
    path('<uuid:organization_id>/baseball/competitions/<uuid:competition_id>/', organization_competition_details),
    path('<uuid:organization_id>/baseball/teams/', organization_team_list),
    path('<uuid:organization_id>/baseball/teams/<uuid:team_id>/', organization_team_details),
]