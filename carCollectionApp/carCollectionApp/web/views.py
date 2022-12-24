from django.shortcuts import render, redirect

from carCollectionApp.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from carCollectionApp.web.models import Profile, Car


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
    return render(request, 'index.html', context)


def catalogue(request):
    cars = Car.objects.all()
    cars_count = len(cars)
    context = {
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'catalogue.html', context)


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
    }
    return render(request, 'profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    total_price_all_cars = sum([c.price for c in Car.objects.all()])
    context = {
        'profile': profile,
        'total_price_all_cars': total_price_all_cars,
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
    return render(request, 'profile-edit.html', context)


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
    return render(request, 'profile-delete.html', context)


def create_car(request):
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()

    context = {
        'form': form,
    }
    return render(request, 'car-create.html', context)


def details_car(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car,
    }
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context)
