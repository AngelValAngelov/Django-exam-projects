from django.shortcuts import render, redirect

from notes_app.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm

from notes_app.web.models import Profile, Note


def home(request):
    profile = Profile.objects.all()
    notes = Note.objects.all()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateProfileForm()
    context = {
        'profile': profile,
        'notes': notes,
        'form': form,
    }
    if not profile:
        return render(request, 'home-no-profile.html', context)
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Note.objects.all().delete()
        return redirect('index')
    else:
        profile = Profile.objects.all()
        notes = Note.objects.all()
        context = {
            'profile': profile[0],
            'notes': notes,
        }
        return render(request, 'profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('index')
