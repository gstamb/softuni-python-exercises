from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from api_app_test.user_auth.forms import UserRegisterForm,CustomerRegisterForm

UserModel = get_user_model()

class HomePageView(TemplateView):
    template_name = "home-with-profile.html"

class UserLogin(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')


def logout(request):
    logout(request)
    return redirect('homepage')


class EntityRegisterView(SuccessMessageMixin, CreateView):
    # handles registration for both users and customers
    template_name = 'registration/register.html'
    success_url = reverse_lazy('homepage')
    model = UserModel
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, self.object)
        return valid

    def dispatch(self, request, *args, **kwargs):
        if request.path == '/register/customer/':
            self.form_class = CustomerRegisterForm
            print("I entered customer")
        else:
            self.form_class = UserRegisterForm
            print("I entered user")
            
        return super().dispatch(request, *args, **kwargs)