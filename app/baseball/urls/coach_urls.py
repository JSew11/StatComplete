from django.urls import path

from ..views.coach_viewset import CoachViewSet

coach_list = CoachViewSet.as_view({
    'get': 'list', 
    'post': 'create'
})

coach_details = CoachViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', coach_list),
    path('<uuid:coach_id>/', coach_details),
]