from django.shortcuts import render, redirect

from gamesPlayApp.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from gamesPlayApp.web.models import Profile, Game


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    if profile:
        context = {
            'profile': profile,
        }
    else:
        context = {
            'no_profile': True,
        }
    return render(request, 'home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile': profile,
        'no_profile': True,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games_count = Game.objects.count()
    games_rating = sum([r.rating for r in Game.objects.all()])
    if games_rating != 0:
        games_rating /= len(Game.objects.all())
    context = {
        'profile': profile,
        'games_count': games_count,
        'games_rating': games_rating,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()

    context = {
        'form': form,
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)
