from django.urls import path

from ..views.organization_viewset import OrganizationViewSet

organization_list = OrganizationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

organization_details = OrganizationViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

organization_competition_list = OrganizationViewSet.as_view({
    'get': 'list_competitions',
    'post': 'create_competition'
})

organization_competition_details = OrganizationViewSet.as_view({
    'get': 'retrieve_competition',
    'patch': 'partial_update_competition',
    'delete': 'destroy_competition'
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
    path('<uuid:organization_id>/competitions/', organization_competition_list),
    path('<uuid:organization_id>/competitions/<uuid:competition_id>/', organization_competition_details),
    path('<uuid:organization_id>/teams/', organization_team_list),
    path('<uuid:organization_id>/teams/<uuid:team_id>/', organization_team_details),
]