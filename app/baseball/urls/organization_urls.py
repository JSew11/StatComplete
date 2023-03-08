from django.urls import path

from ..views.organization_competition_details import OrganizationCompetitionDetails
from ..views.organization_competition_list import OrganizationCompetitionList
from ..views.organization_list import OrganizationList
from ..views.organization_details import OrganizationDetails

urlpatterns = [
    path('', OrganizationList.as_view()),
    path('<uuid:organization_id>/', OrganizationDetails.as_view()),
    path('<uuid:organization_id>/competitions/', OrganizationCompetitionList.as_view()),
    path('<uuid:organization_id>/competitions/<uuid:competition_id>/', OrganizationCompetitionDetails.as_view()),
]