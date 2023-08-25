from django.shortcuts import render, redirect

from django101.testing.forms.profile import ProfileForm
from django101.testing.models import Profile


def index(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        form = ProfileForm()
        context = {
            'profiles': profiles,
            'form': form,
        }
        return render(request, 'testing/index.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles')

        profiles = Profile.objects.all()
        context = {
            'profiles': profiles,
            'form': form,
        }

        return render(request, 'testing/index.html', context)
