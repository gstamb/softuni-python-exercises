from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages


class LoggedInPermissionsMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(self.request, 'You must be logged in')
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
 
        if not self.has_permission():
            permission_type  = self.permission_required.split(".")[1][:-5]
            messages.warning(self.request, f'You must complete your profile before {permission_type}ing a trip.')
            return HttpResponseRedirect(reverse_lazy('edit profile' , kwargs={'pk': request.user.id}))
        return super(LoggedInPermissionsMixin, self).dispatch(request, *args, **kwargs)
