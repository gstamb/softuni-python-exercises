from django.shortcuts import render, redirect
from plantapp.core.utils import get_profile, get_all_plants
from plantapp.user_profile.forms import ProfileCreateForm, ProfileEditForm


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def show_profile(request):
    profile = get_profile()
    form = ProfileCreateForm(instance=profile)
    plants = get_all_plants()[:3]
    context = {
        'form': form,
        'profile': profile,
        'plants': plants
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show-profile')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        all_posts = get_all_plants()
        if all_posts:
            for post in all_posts:
                post.delete()
        return redirect('show-index')

    context = {
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
