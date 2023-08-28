from django.shortcuts import redirect, render
from fruitpedia.fruit.forms import FruitCreateForm
from fruitpedia.user_profile.models import UserProfile
from fruitpedia.fruit.models import FruitModel



def index(request):
    user_profile = UserProfile.objects.first()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'index.html', context)


def dashboard(request):
    user_profile = UserProfile.objects.first()
    fruits = FruitModel.objects.all()
    context = {
        'fruits': fruits,
        'user_profile': user_profile
    }
    return render(request, 'dashboard.html', context)


def fruit_details(request, pk):
    user_profile = UserProfile.objects.first()
    context = {
        'user_profile': user_profile,
        'fruit': FruitModel.objects.get(pk=pk)
    }
    return render(request, 'details-fruit.html', context)


def create_fruit(request):
    user_profile = UserProfile.objects.first()
    if request.method == 'GET':
        form = FruitCreateForm(instance=FruitModel())
        context = {
            'user_profile': user_profile,
            'form': form
        }
        return render(request, 'create-fruit.html', context)
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            new_fruit = FruitModel(**form.cleaned_data)
            new_fruit.save()
            return redirect('dashboard')
        else:
            context = {
                'user_profile': user_profile,
                'form': form
            }
        return render(request, 'create-fruit.html', context)


def delete_fruit(request, pk):
    user_profile = UserProfile.objects.first()
    fruit = FruitModel.objects.get(pk=pk)
    form = FruitCreateForm(instance=fruit)
    if request.method == 'GET':

        for fieldname in form.fields:
            form.fields[fieldname].disabled = True
        context = {
            'user_profile': user_profile,
            'fruit': fruit,
            'form': form
        }
        return render(request, 'delete-fruit.html', context)
    else:
        fruit.delete()
        return redirect('dashboard')


def edit_fruit(request, pk):
    user_profile = UserProfile.objects.first()
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = FruitCreateForm(instance=fruit)
        context = {
            'user_profile': user_profile,
            'form': form,
            'fruit': fruit
        }
        return render(request, 'edit-fruit.html', context)

    else:
        form = FruitCreateForm(request.POST, instance=fruit)
        if form.is_valid():
            new_fruit = form.save()
            return redirect('dashboard')
        else:
            context = {
                'user_profile': user_profile,
                'form': form,
                'fruit': fruit
            }
        return render(request, 'edit-fruit.html', context)