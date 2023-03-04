from django.urls import path

from ..views.coach_details import CoachDetails
from ..views.coach_list import CoachList

urlpatterns = [
    path('', CoachList.as_view()),
    path('<uuid:coach_id>/', CoachDetails.as_view()),
]