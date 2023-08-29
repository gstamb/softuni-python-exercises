from django.shortcuts import redirect, render
from fruitpedia.fruit.forms import FruitCreateForm, FruitDeleteForm
from fruitpedia.fruit.models import FruitModel
from fruitpedia.core.utils import get_profile, get_all_fruits


def index(request):
    user_profile = get_profile()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'index.html', context)


def dashboard(request):
    user_profile = get_profile()
    fruits = get_all_fruits()
    context = {
        'fruits': fruits,
        'user_profile': user_profile
    }
    return render(request, 'dashboard.html', context)


def fruit_details(request, pk):
    user_profile = get_profile()
    fruit = FruitModel.objects.get(pk=pk)
    context = {
        'user_profile': user_profile,
        'fruit': fruit
    }
    return render(request, 'details-fruit.html', context)


def add_fruit(request):
    user_profile = get_profile()
    form = FruitCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'create-fruit.html', context)


def delete_fruit(request, pk):
    user_profile = get_profile()
    fruit = FruitModel.objects.get(pk=pk)
    form = FruitDeleteForm(instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')
    context = {
        'user_profile': user_profile,
        'fruit': fruit,
        'form': form
    }
    return render(request, 'delete-fruit.html', context)


def edit_fruit(request, pk):
    user_profile = get_profile()
    fruit = FruitModel.objects.get(pk=pk)
    form = FruitCreateForm(instance=fruit)

    if request.method == 'POST':
        form = FruitCreateForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'user_profile': user_profile,
        'form': form,
        'fruit': fruit
    }
    return render(request, 'edit-fruit.html', context)
