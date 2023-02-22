"""statcomplete_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from baseball.views.competition_details import CompetitionDetails
from baseball.views.competition_list import CompetitionList
from baseball.views.coach_details import CoachDetails
from baseball.views.coach_list import CoachList
from baseball.views.player_details import PlayerDetails
from baseball.views.player_list import PlayerList

urlpatterns = [
    path('competitions/', CompetitionList.as_view()),
    path('competitions/<uuid:competition_id>/', CompetitionDetails.as_view()),
    path('coaches/', CoachList.as_view()),
    path('coaches/<uuid:coach_id>/', CoachDetails.as_view()),
    path('players/', PlayerList.as_view()),
    path('players/<uuid:player_id>/', PlayerDetails.as_view()),
    path('admin/', admin.site.urls),
]
