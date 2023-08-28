from django.shortcuts import redirect, render
from fruitpedia.fruit.models import FruitModel
from fruitpedia.user_profile.forms import UserCreateForm, UserEditForm
from fruitpedia.user_profile.models import UserProfile
from django.contrib.auth.hashers import make_password

def create_profile(request):
    user_profile = UserProfile.objects.first()
    form = UserCreateForm()
    if request.method == 'GET':

        context = {
            'user_profile': user_profile,
            'form': form
        }
        return render(request, 'create-profile.html', context)
    else:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = UserProfile(**form.cleaned_data)
            new_user.password = make_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('index')
        else:
            context = {
                'user_profile': user_profile,
                'form': form
            }
            return render(request, 'create-profile.html', context)


def profile_details(request):
    posts = FruitModel.objects.all()
    user_profile = UserProfile.objects.first()
    context = {
        'user_profile': user_profile,
        'posts': len(posts)
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request, pk):
    user_profile = UserProfile.objects.first()
    user_profile_filtered = UserProfile.objects.filter(pk=pk).values(
        'first_name', 'last_name', 'email', 'image_url')
    form = UserEditForm(user_profile_filtered[0])
    form.fields['password'].widget.attrs['hidden'] = True
    if request.method == 'GET':
        context = {
            'user_profile': user_profile,
            'form': form
        }
        return render(request, 'edit-profile.html', context)
    else:
        form = UserEditForm(request.POST)
        if form.is_valid():
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.email = form.cleaned_data['email']
            user_profile.image_url = form.cleaned_data['image_url']
            user_profile.save()
            return redirect('dashboard')
        else:
            context = {
                'user_profile': user_profile,
                'form': form
            }
            return render(request, 'edit-profile.html', context)


def delete_profile(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'user_profile': user_profile
        }
        return render(request, 'delete-profile.html', context)
    else:
        user_profile.delete()
        for fruit in FruitModel.objects.all():
            fruit.delete()
        return redirect('index')