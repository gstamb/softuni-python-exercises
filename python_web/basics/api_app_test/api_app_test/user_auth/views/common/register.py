from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model

from api_app_test.user_auth.forms.customer.create import CustomerRegisterForm
from api_app_test.user_auth.forms.user.create import UserRegisterForm

UserModel = get_user_model()


class EntityRegisterView(SuccessMessageMixin, CreateView):
    # handles registration for both users and customers
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
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
