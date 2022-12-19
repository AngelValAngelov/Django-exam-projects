from django.shortcuts import render, redirect

from myMusicApp.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from myMusicApp.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()
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
        'albums': albums,
    }
    if profile:
        return render(request, 'home-with-profile.html', context)
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateAlbumForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
        'profile': profile,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
        'profile': profile,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    profile = get_profile()
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
        'profile': profile,
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        Profile.objects.all().delete()
        Album.objects.all().delete()
        return redirect('index')
    return render(request, 'profile-delete.html', context={'profile': profile})

