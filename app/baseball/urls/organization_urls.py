from django.urls import path

from ..views.organization_list import OrganizationList
from ..views.organization_details import OrganizationDetails

urlpatterns = [
    path('', OrganizationList.as_view()),
    path('<uuid:organization_id>/', OrganizationDetails.as_view()),
]