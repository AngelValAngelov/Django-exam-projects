from django.shortcuts import render, redirect

from myPlantApp.web.forms import CreateProfileForm, CreatePlantForm, EditPlantForm, DeletePlantForm, EditProfileForm, \
    DeleteProfileForm
from myPlantApp.web.models import Profile, Plant


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
            'has_profile': True,
        }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'has_profile': True,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    profile_stars = Plant.objects.count()
    context = {
        'profile': profile,
        'profile_stars': profile_stars,

    }
    return render(request, 'profile-details.html', context)


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
    }
    return render(request, 'delete-profile.html', context)


def catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants,
    }
    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
    }
    return render(request, 'create-plant.html', context)


def details_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    context = {
        'plant': plant,
    }
    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeletePlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'delete-plant.html', context)
