from django.urls import path

from users.views import (
    UserRegisterView,
    UserProfileView,
    UserLoginView,
    logout_view,
)

app_name = 'users'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
]
