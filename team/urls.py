from django.urls import path
from . import views


urlpatterns = [
    path('', views.teams, name='teams'),
    path('<str:name>/players/', views.players, name='players'),
    path('<str:name>/player/add/', views.player_add, name='player_add'),
    path('<str:name>/edit_details/', views.player_edit, name='player_edit'),
    path('player/delete/<int:id>/', views.player_delete, name='player_delete'),


    path('<str:name>/stats/', views.playerHistory_details,
         name="playerHistory_details"),
    path('<str:name>/add_stats/',
         views.playerHistory_add, name="playerHistory_add"),
    path('<str:name>/edit_stats/',
         views.playerHistory_edit, name="playerHistory_edit"),

    path('matchesList/', views.matchesList, name='matches_list'),
    path('matches/add/', views.matchesAdd, name="matches_add"),

    path('points/', views.pointsView, name='points'),
]
