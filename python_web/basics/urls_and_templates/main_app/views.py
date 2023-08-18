from django.shortcuts import render


def index(request):
    return render(request, 'primary_app_index.html')
