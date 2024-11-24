from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect('products:index')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('products:index')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('products:index')
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'


class UserProfileView(UpdateView):
    form_class = UserProfileForm
    queryset = User.objects.all()
    template_name = 'users/profile.html'
    success_url = reverse_lazy('products:index')

