from django.shortcuts import redirect, render
from django.urls import reverse
from carcollection.car_app.forms.profile_forms import ProfileCreateForm, ProfileEditForm
from django.contrib.auth.hashers import make_password
from django.db.models import Sum
from carcollection.car_app.models.car_model import Car
from carcollection.car_app.models.user_model import Profile


def create_profile(request):
    form = ProfileCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.password = make_password(new_profile.password)
            new_profile.save()
            return redirect('catalogue')
    context = {

        'form': form
    }
    return render(request, 'profile-create.html', context)


def details_profile(request):
    cars_value = Car.objects.aggregate(Sum('price'))
    formatted_cars_value = '{0:.3f}'.format(cars_value['price__sum'] or 0)
    context = {
        'cars_value': formatted_cars_value
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            edited_profile = form.save(commit=False)
            edited_profile.password = make_password(
                form.cleaned_data['password'])
            edited_profile.save()
            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        [car.delete() for car in Car.objects.all()]
        profile.delete()
        return redirect('index')

    return render(request, 'profile-delete.html')
