from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from music_app.authentication.forms import RegisterForm
from music_app.user.models import Profile
from django.contrib.auth.models import User


 

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=User())
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = Profile(username=user, email=user.email)
            profile.save()
            return redirect('user home')
    return render(request, 'home-no-profile.html', {'form': form, 'template_name': 'partials/create_form.html'})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('user home')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('user home')

    return render(request, 'home-no-profile.html', {'form': form, 'template_name': 'partials/login_form.html'})
