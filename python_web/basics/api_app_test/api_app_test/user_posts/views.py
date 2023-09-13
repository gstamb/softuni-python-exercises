from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from api_app_test.user_posts.forms import TripForm
from api_app_test.user_posts.models import Trip, TripImage
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


class CreateTripView(CreateView):
    # Creates a trip and allows for multiple images to be uploaded.
    # A default image object holding a default image will be created if no image is provided
    model = Trip
    fields = ["title", "country", "city", "review", "rating"]
    template_name = 'add-trip.html'
    success_url = reverse_lazy('user trips')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        images = self.request.FILES.getlist('images')
        if images:
            for image in images:
                TripImage.objects.create(trip=self.object, images=image)
        else:
            TripImage.objects.create(trip=self.object)
        return response


class ShowUserTrips(ListView):
    # creates filtered pagination for a model whereas user matches the owner id
    model = Trip
    paginate_by = 4
    template_name = "homepage.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class ShowAllUserTrips(ListView):
    # creates filtered pagination for a model whereas user is not the owner id
    model = Trip
    paginate_by = 4
    template_name = "homepage.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(author=self.request.user)




# def add_trip(request):
#     trip_form = TripForm()
#     if request.method == "POST":
#         trip_form = TripForm(request.POST, request.FILES)
#         images = request.FILES.getlist('images')

#         if trip_form.is_valid():
#             trip = trip_form.save(commit=False)
#             trip.author = request.user
#             trip.save()

#             if images:
#                 for image in images:
#                     TripImage.objects.create(
#                         trip=trip,
#                         images=image,
#                     )
#             else:
#                 TripImage.objects.create(trip=trip)

#             return redirect('homepage')
#     else:
#         trip_form = TripForm()

#     return render(request, 'add-trip.html', {'trip_form': trip_form})
