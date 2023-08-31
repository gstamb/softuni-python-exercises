from django.shortcuts import render
from carcollection.car_app.models.car_model import Car


def index(request):
    return render(request, 'index.html')


def catalogue(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
        'cars_cnt': len(cars)
    }
    return render(request, 'catalogue.html', context)
