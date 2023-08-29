from fruitpedia.fruit.models import FruitModel
from fruitpedia.user_profile.models import UserProfile


def get_profile():
    return UserProfile.objects.first()

def get_all_fruits():
    return FruitModel.objects.all() if FruitModel.objects.all() else None