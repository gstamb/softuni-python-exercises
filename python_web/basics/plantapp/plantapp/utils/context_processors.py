from plantapp.user_profile.models import ProfileModel


def profile_context(request):
    profile = None
    if request.user.is_authenticated:
        profile = ProfileModel.objects.first()
    return {'profile': profile}
