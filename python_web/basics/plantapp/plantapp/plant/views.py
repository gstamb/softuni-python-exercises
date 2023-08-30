from django.shortcuts import render, redirect
from plantapp.core.utils import get_all_plants
from plantapp.plant.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from plantapp.plant.models import PlantModel


def show_homepage(request):
    return render(request, 'home-page.html')


def show_catalogue(request):
    plants = get_all_plants()
    context = {'plants': plants}
    return render(request, 'catalogue.html', context)


def create_plant(request):
    form = PlantCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')
    context = {'form': form}
    return render(request, 'create-plant.html', context)


def show_details(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    context = {'plant': plant}
    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    form = PlantEditForm(instance=plant)
    if request.method == 'POST':
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')

    context = {'plant': plant, 'form': form}
    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    plant = PlantModel.objects.get(pk=pk)
    form = PlantDeleteForm(instance=plant)
    if request.method == 'POST':
        plant.delete()
        return redirect('show-catalogue')

    context = {'plant': plant, 'form': form}
    return render(request, 'delete-plant.html', context)
