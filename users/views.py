from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from products.models import Basket
from products.services import get_total_sum
from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect("products:index")


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("products:index")


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:login")
    success_message = "%(username)s was created successfully"


@method_decorator(login_required, name="dispatch")
class UserProfileView(UpdateView):
    form_class = UserProfileForm
    queryset = User.objects.all()
    template_name = "users/profile.html"
    success_url = reverse_lazy("products:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = Basket.objects.filter(user=self.object)
        # Can use context_processor to pass baskets to template
        # context['baskets'] = baskets
        context["title"] = "Profile"
        context["total_sum"] = get_total_sum(baskets)
        return context
