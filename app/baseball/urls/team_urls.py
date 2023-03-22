from django.urls import path

from ..views.team_viewset import TeamViewSet

team_list = TeamViewSet.as_view({
    'get': 'list'
})

team_details = TeamViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', team_list),
    path('<uuid:team_id>/', team_details),
]