from carcollection.car_app.models.user_model import Profile


def profile_context(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.first()
    return {'profile': profile}
