from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from api_app_test.data_profile.forms import CustomerUpdateForm, UserUpdateForm
from api_app_test.data_profile.models import CustomerProfile, UserProfile
from api_app_test.user_auth.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name_suffix = "-edit"

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('show profile', kwargs={'pk': userid})

    def get_object(self):
        user = self.request.user
        if user.role == 'customer':
            return CustomerProfile.objects.get(email=user)
        else:
            return UserProfile.objects.get(email=user)

    def get_form_class(self):
        user = self.request.user
        if user.role == 'customer':
            return CustomerUpdateForm
        else:
            return UserUpdateForm

    def form_valid(self, form):
        form.instance.email = self.request.user
        image = self.request.FILES.get('image')
        form.instance.image_url = image
        return super().form_valid(form)


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    exclude_fields = ['id', 'image_url']
    model = CustomUser
    template_name = 'data_profile/profile-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        try:
            if user.role == 'customer':
                profile = CustomerProfile.objects.get(email=user)
            else:
                profile = UserProfile.objects.get(email=user)

            field_names = [field.name for field in profile._meta.get_fields(
            ) if field.name not in self.exclude_fields]

        except (CustomerProfile.DoesNotExist, UserProfile.DoesNotExist):
            profile = None
            field_names = []

        context['profile'] = profile
        context['field_names'] = field_names
        return context


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('homepage')
    template_name = "data_profile/profile-delete.html"
