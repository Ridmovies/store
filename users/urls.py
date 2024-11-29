from django.urls import path

from users.views import (
    UserLoginView,
    UserProfileView,
    UserRegisterView,
    logout_view,
    EmailVerificationView,
)

app_name = "users"

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegisterView.as_view(), name="registration"),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    path("<int:pk>/profile/", UserProfileView.as_view(), name="profile"),
]
