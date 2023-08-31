from django.shortcuts import redirect, render

from carcollection.car_app.forms.car_forms import CarCreateForm, CarEditForm, CarDeleteForm
from carcollection.car_app.models.car_model import Car


def add_car(request):
    form = CarCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form
    }
    return render(request, 'car-create.html', context)


def details_car(request, pk):
    car = Car.objects.get(pk=pk)
    context = {
        'car': car
    }
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarEditForm(instance=car)
    if request.method == 'POST':
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'car': car,
        'form': form
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarDeleteForm(instance=car)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'car': car,
        'form': form
    }
    return render(request, 'car-delete.html', context)
