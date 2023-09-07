from django.shortcuts import render
from music_app.albums.models import Album
from music_app.authentication.forms import RegisterForm
from music_app.user.forms import ProfileForm
from music_app.user.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from music_app.authentication.views import register


# Create your views here.
def user_home(request):
    albums = Album.objects.filter(users=request.user)
    context = {
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context )


def show_profile(request):
    profile = Profile.objects.get(username=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'profile-details.html', context)

def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'profile-delete.html')