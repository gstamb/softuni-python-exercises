from django.shortcuts import redirect, render
from fruitpedia.fruit.models import FruitModel
from fruitpedia.user_profile.forms import UserCreateForm, UserEditForm
from fruitpedia.user_profile.models import UserProfile
from django.contrib.auth.hashers import make_password
from fruitpedia.core.utils import get_profile, get_all_fruits


def create_profile(request):
    user_profile = get_profile()
    form = UserCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = get_profile()
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('dashboard')

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    user_profile = get_profile()
    posts_count = FruitModel.objects.count()
    context = {
        'user_profile': user_profile,
        'posts_count': posts_count
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    user_profile = get_profile()
    form = UserEditForm(instance=user_profile)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        user_profile.delete()
        fruits = get_all_fruits()
        if fruits:
            for fruit in fruits:
                fruit.delete()
        return redirect('index')

    context = {
        'user_profile': user_profile
    }
    return render(request, 'delete-profile.html', context)
