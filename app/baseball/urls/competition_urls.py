from django.urls import path

from ..views.competition_viewset import CompetitionViewSet

competition_list = CompetitionViewSet.as_view({
    'get': 'list'
})

competition_details = CompetitionViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', competition_list),
    path('<uuid:competition_id>/', competition_details),
]