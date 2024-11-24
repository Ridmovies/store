from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect('products:index')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('products:index')
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'
