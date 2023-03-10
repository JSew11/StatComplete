from django.urls import path

from ..views.organization_viewset import OrganizationViewSet
from ..views.organization_team_list import OrganizationTeamList
from ..views.organization_team_details import OrganizationTeamDetails

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

urlpatterns = [
    path('', organization_list),
    path('<uuid:organization_id>/', organization_details),
    path('<uuid:organization_id>/competitions/', organization_competition_list),
    path('<uuid:organization_id>/competitions/<uuid:competition_id>/', organization_competition_details),
    path('<uuid:organization_id>/teams/', OrganizationTeamList.as_view()),
    path('<uuid:organization_id>/teams/<uuid:team_id>/', OrganizationTeamDetails.as_view()),
]