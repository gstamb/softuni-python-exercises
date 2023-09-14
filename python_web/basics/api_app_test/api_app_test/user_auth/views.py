from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from api_app_test.user_auth.forms import UserRegisterForm, CustomerRegisterForm


class HomePageView(TemplateView):
    template_name = "trips/homepage.html"


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')


class logOut(View):
    def get(self, request):
        logout(request)
        return redirect('homepage')


class EntityRegisterView(SuccessMessageMixin, CreateView):
    # Handles registration for both users and customers
    template_name = 'registration/register.html'
    success_url = reverse_lazy('homepage')
    model = get_user_model()
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, self.object)
        return valid

    def dispatch(self, request, *args, **kwargs):
        if request.path == '/register/customer/':
            self.form_class = CustomerRegisterForm
        else:
            self.form_class = UserRegisterForm

        return super().dispatch(request, *args, **kwargs)
