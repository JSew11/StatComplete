from django.urls import path

from ..views.organization_viewset import OrganizationViewSet
from ..views.organization_competition_details import OrganizationCompetitionDetails
from ..views.organization_competition_list import OrganizationCompetitionList
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

urlpatterns = [
    path('', organization_list),
    path('<uuid:organization_id>/', organization_details),
    path('<uuid:organization_id>/competitions/', OrganizationCompetitionList.as_view()),
    path('<uuid:organization_id>/competitions/<uuid:competition_id>/', OrganizationCompetitionDetails.as_view()),
    path('<uuid:organization_id>/teams/', OrganizationTeamList.as_view()),
    path('<uuid:organization_id>/teams/<uuid:team_id>/', OrganizationTeamDetails.as_view()),
]