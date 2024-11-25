from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView

from products.models import Basket
from products.services import get_total_sum
from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect('products:index')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('products:index')


class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = "%(username)s was created successfully"

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     # Отправляем сообщение об успешном завершении регистрации
    #     messages.success(self.request, 'Вы успешно зарегистрировались. Можете войти на сайт!')
    #     return response


@method_decorator(login_required, name='dispatch')
class UserProfileView(UpdateView):
    form_class = UserProfileForm
    queryset = User.objects.all()
    template_name = 'users/profile.html'
    success_url = reverse_lazy('products:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        baskets = Basket.objects.filter(user=self.object)
        context['title'] = "Profile"
        context['baskets'] = baskets
        context['total_sum'] = get_total_sum(baskets)
        return context
