from django.contrib.auth.views import LoginView
from django.urls import path

from users.views import (
    logout_view,
    UserRegisterView,
    UserProfileView,
    UserLoginView,
)

app_name = 'users'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    # path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
]
