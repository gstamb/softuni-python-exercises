from plantapp.plant.models import PlantModel
from plantapp.user_profile.models import ProfileModel

def get_profile():
    return ProfileModel.objects.first()

def get_all_plants():
    return PlantModel.objects.all()