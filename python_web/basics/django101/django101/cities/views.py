from django.shortcuts import render, redirect
from django101.cities.models import Person


def index(req):
    context = {
        "name": "Georgi",
        "people": Person.objects.all(),
    }
    return render(req, 'index.html', context)


def list_phones(request):
    context = {
        "message": "This is the list of available phones",
        'phones': {"Galaxy S5000": {'product_id': 245, 'quantity': 3},
                   "Xaomi redmi 5": {'product_id': 241, 'quantity': 0},
                   "Iphone 12": {'product_id': 243, 'quantity': 1},
                   }

    }

    return render(request, 'phones.html', {"phones": context})


def create_person(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
    Person(
        name=name,
        age=age
    ).save()
    return redirect('/cities')
