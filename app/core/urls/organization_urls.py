from django.urls import path

from ..views.organization_viewset import OrganizationViewSet
from ..views.organization_baseball_viewset import OrganizationBaseballCompetitionViewset

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

organization_team_list = OrganizationViewSet.as_view({
    'get': 'list_teams',
    'post': 'create_team'
})

organization_team_details = OrganizationViewSet.as_view({
    'get': 'retrieve_team',
    'patch': 'partial_update_team',
    'delete': 'destroy_team'
})

urlpatterns = [
    path('', organization_list),
    path('<uuid:organization_id>/', organization_details),
    path('<uuid:organization_id>/baseball/competitions/', organization_competition_list),
    path('<uuid:organization_id>/baseball/competitions/<uuid:competition_id>/', organization_competition_details),
    path('<uuid:organization_id>/baseball/teams/', organization_team_list),
    path('<uuid:organization_id>/baseball/teams/<uuid:team_id>/', organization_team_details),
]