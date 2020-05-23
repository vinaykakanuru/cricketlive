from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
from .forms import *
from collections import Counter

# Create your views here.


def teams(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, 'team/team.html', context)


def players(request, name=None):
    context = {}
    context['team'] = get_object_or_404(Team, name=name)
    return render(request, 'team/players.html', context)


def player_add(request, name=None):
    team = get_object_or_404(Team, name=name)
    context = {}
    context['team'] = team
    if request.method == 'POST':
        player_form = PlayerForm(request.POST, request.FILES)
        context['player_form'] = player_form
        if player_form.is_valid():
            u = player_form.save()
            return HttpResponseRedirect(reverse('players', args=(team.name,)))
        else:
            return render(request, 'team/player_add.html', context)
    else:
        player_form = PlayerForm()
        context['player_form'] = player_form
        return render(request, 'team/player_add.html', context)


def player_edit(request, name=None):
    player = get_object_or_404(Player, firstName=name)
    team = get_object_or_404(Team, id=player.team.id)
    context = {}
    context['player'] = player
    if request.method == 'POST':
        playeredit_form = PlayerForm(
            request.POST, instance=player)
        context['playeredit_form'] = playeredit_form
        if playeredit_form.is_valid():
            playeredit_form.save()
            return HttpResponseRedirect(reverse('players', args=(team.name,)))
        else:
            return render(request, 'team/player_edit.html', context)
    else:
        playeredit_form = PlayerForm(instance=player)
        context['playeredit_form'] = playeredit_form
        return render(request, 'team/player_edit.html', context)


def player_delete(request, id=None):
    player = get_object_or_404(Player, id=id)
    team = get_object_or_404(Team, id=player.team.id)
    player.delete()
    return HttpResponseRedirect(reverse('players', args=(team.name,)))


def playerHistory_details(request, name=None):
    player = get_object_or_404(Player, firstName=name)
    try:
        playerHistory = PlayerHistory.objects.get(player__pk=player.id)
    except:
        return HttpResponseRedirect(reverse('playerHistory_add', args=(player.firstName,)))

    context = {}
    context['player'] = player
    context['playerHistory'] = playerHistory
    return render(request, 'team/playerhistory_details.html', context)


def playerHistory_add(request, name=None):
    player = get_object_or_404(Player, firstName=name)
    team = get_object_or_404(Team, id=player.team.id)
    context = {}
    context['player'] = player
    if request.method == 'POST':
        playerhistory_form = PlayerHistoryForm(request.POST)
        context['playerhistory_form'] = playerhistory_form
        if playerhistory_form.is_valid():
            u = playerhistory_form.save()
            return HttpResponseRedirect(reverse('players', args=(team.name,)))
        else:
            return render(request, 'team/playerhistory_add.html', context)
    else:
        playerhistory_form = PlayerHistoryForm()
        context['playerhistory_form'] = playerhistory_form
        return render(request, 'team/playerhistory_add.html', context)


def playerHistory_edit(request, name=None):
    player = get_object_or_404(Player, firstName=name)
    team = get_object_or_404(Team, id=player.team.id)
    playerHistory = PlayerHistory.objects.get(player__pk=player.id)
    context = {}
    context['player'] = player
    if request.method == 'POST':
        playerhistory_form = PlayerHistoryForm(
            request.POST, instance=playerHistory)

        context['playerhistory_form'] = playerhistory_form
        if playerhistory_form.is_valid():
            playerhistory_form.save()
            return HttpResponseRedirect(reverse('players', args=(team.name,)))
        else:
            return render(request, 'team/playerhistory_edit.html', context)
    else:
        playerhistory_form = PlayerHistoryForm(instance=playerHistory)
        context['playerhistory_form'] = playerhistory_form
        return render(request, 'team/playerhistory_edit.html', context)


def matchesList(request):
    matches = Matches.objects.all()
    context = {'matches': matches}
    return render(request, 'team/matches.html', context)


def matchesAdd(request):
    context = {}
    if request.method == 'POST':
        match_form = MatchForm(request.POST)
        context['match_form'] = match_form
        if match_form.is_valid():
            u = match_form.save()
            return HttpResponseRedirect(reverse('matches_list'))
        else:
            return render(request, 'team/matches_add.html', context)
    else:
        match_form = MatchForm()
        context['match_form'] = match_form
        return render(request, 'employee/matches_add.html', context)


def pointsView(request):
    points = PointsTable.objects.values_list()
    l = [i[1] for i in points]
    points = Counter(l)
    context = {'points': sorted(
        points.items(), key=lambda x: x[1], reverse=True)}

    return render(request, 'team/points.html', context)
