from django.urls import path

from ..views.player_viewset import PlayerViewSet

player_list = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

player_details = PlayerViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', player_list),
    path('<uuid:player_id>/', player_details),
]