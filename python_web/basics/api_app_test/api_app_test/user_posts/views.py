from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from api_app_test.user_posts.forms import TripForm, TripImageForm
from api_app_test.user_posts.models import Trip, TripImage


def add_trip(request):
    TripImageFormSet = inlineformset_factory(
        Trip, TripImage, form=TripImageForm, extra=1, can_delete=False)

    if request.method == "POST":
        trip_form = TripForm(request.POST, request.FILES)
        formset = TripImageFormSet(request.POST, request.FILES)

        if trip_form.is_valid() and formset.is_valid():
            trip = trip_form.save(commit=False)
            trip.author = request.user
            trip.save()

            instances = formset.save(commit=False)
            for instance in instances:
                instance.trip = trip
                instance.save()
            return redirect('homepage')
    else:
        trip_form = TripForm()
        formset = TripImageFormSet()

    return render(request, 'add-trip.html', {'trip_form': trip_form, 'formset': formset})
