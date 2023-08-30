from django.shortcuts import render, redirect
from plantapp.core.utils import get_profile, get_all_plants
from plantapp.plant.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from plantapp.plant.models import PlantModel


def show_homepage(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'home-page.html', context)


def show_catalogue(request):
    profile = get_profile()
    plants = get_all_plants()
    context = {'profile': profile, 'plants': plants}
    return render(request, 'catalogue.html', context)


def create_plant(request):
    profile = get_profile()
    form = PlantCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')
    context = {'profile': profile, 'form': form}
    return render(request, 'create-plant.html', context)


def show_details(request, pk):
    profile = get_profile()
    plant = PlantModel.objects.get(pk=pk)
    context = {'profile': profile, 'plant': plant}
    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):
    profile = get_profile()
    plant = PlantModel.objects.get(pk=pk)
    form = PlantEditForm(instance=plant)
    if request.method == 'POST':
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')

    context = {'profile': profile, 'plant': plant, 'form': form}
    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    profile = get_profile()
    plant = PlantModel.objects.get(pk=pk)
    form = PlantDeleteForm(instance=plant)
    if request.method == 'POST':
        plant.delete()
        return redirect('show-catalogue')

    context = {'profile': profile, 'plant': plant, 'form': form}
    return render(request, 'delete-plant.html', context)
