from django.urls import path, include

urlpatterns = [
    path('organizations/', include('baseball.urls.organization_urls')),
    path('competitions/', include('baseball.urls.competition_urls')),
    path('coaches/', include('baseball.urls.coach_urls')),
    path('players/', include('baseball.urls.player_urls')),
    path('teams/', include('baseball.urls.team_urls')),
]
