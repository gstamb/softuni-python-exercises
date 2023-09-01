from games_play_app.play_app.models.profile_model import Profile


def return_profile_context(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.first()
    return {'profile': profile}
