from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from api_app_test.data_profile.models import CustomerProfile, UserProfile
from api_app_test.user_auth.models import CustomUser

# Create your views here.

class ProfileUpdateView(UpdateView):
    fields = '__all__'
    template_name_suffix = ""
    
    def get_success_url(self):
            userid=self.kwargs['pk']
            return reverse_lazy('show profile', kwargs={'pk': userid })
      
    def get_object(self):
        user = self.request.user
        if user.role == 'customer':
            return CustomerProfile.objects.get(email=user)
        else:
            return UserProfile.objects.get(email=user)

class ProfileDetailsView(DetailView):
    exclude_fields  = ['id', 'image_url']
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

            field_names = [field.name for field in profile._meta.get_fields() if field.name not in self.exclude_fields]

        except (CustomerProfile.DoesNotExist, UserProfile.DoesNotExist):
            profile = None
            field_names = []

        context['profile'] = profile
        context['field_names'] = field_names
        return context


class ProfileDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('homepage')
    template_name = "data_profile/profile-delete.html"