from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from api_app_test.user_posts.mixins import LoggedInPermissionsMixin
from api_app_test.user_posts.models import Trip, TripImage
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from api_app_test.utils.images_resizing import resize_image
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateTripView(LoggedInPermissionsMixin, CreateView):
    # Creates a trip and allows for multiple images to be uploaded.
    # A default image object holding a default image will be created if no image is provided
    model = Trip
    fields = ["title", "country", "city", "review", "rating"]
    template_name = 'trips/add-trip.html'
    success_url = reverse_lazy('user trips')
    permission_required = 'user_posts.add_trip'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        images = self.request.FILES.getlist('images')
        if images:
            for photo in images:
                TripImage.objects.create(
                    trip=self.object, photo=photo, thumbnail=resize_image(photo))

        else:
            TripImage.objects.create(trip=self.object)
        return response


class ShowUserTrips(LoginRequiredMixin, ListView):
    # creates filtered pagination for a model whereas user matches the owner id
    model = Trip
    paginate_by = 4
    template_name = "trips/homepage.html"
    permission_required = 'user_posts.view_trip'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class ShowAllUserTrips(LoginRequiredMixin, ListView):
    # creates filtered pagination for a model whereas user is not the owner id
    model = Trip
    paginate_by = 4
    template_name = "trips/homepage.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(author=self.request.user)


class ShowTripDetails(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = "trips/details-trip.html"
    context_object_name = "trip"


class UpdateTripView(LoginRequiredMixin, UpdateView):
    # Updates trip data and deletes old files from the filesystem
    model = Trip
    fields = ["title", "country", "city", "review", "rating"]
    template_name = 'trips/update-trip.html'
    success_url = reverse_lazy('user trips')
    permission_required = 'user_posts.change_trip'

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in self.object.photo.all():
            new_image = self.request.FILES.get(f'image_{image.id}')
            if new_image:
                if new_image != image.photo:
                    image.photo.delete(save=False)
                    image.thumbnail.delete(save=False)
                    image.photo = new_image
                    image.thumbnail = resize_image(new_image)
                    image.save()
        return response


class DeleteTripView(LoggedInPermissionsMixin, DeleteView):
    # Deletes the Trip and related images and thumbnails
    model = Trip
    template_name = "trips/delete-trip.html"
    success_url = reverse_lazy('user trips')
    permission_required = 'user_posts.delete_trip'

    def form_valid(self, form):
        success_url = self.get_success_url()
        trip = self.object
        for image in trip.photo.all():
            image.photo.delete(save=True)
            image.thumbnail.delete(save=True)

        trip.delete()
        return HttpResponseRedirect(success_url)
