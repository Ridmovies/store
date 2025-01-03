import uuid
from datetime import timedelta

from django import forms
from django.conf import settings
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from django.core.mail import send_mail
from django.utils.timezone import now

from users.models import User, EmailVerification
from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите пароль"}
        )
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите имя"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите фамилию"}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите имя пользователя",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control py-4",
                "placeholder": "Введите адрес эл. почты",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control py-4", "placeholder": "Введите пароль"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control py-4", "placeholder": "Подтвердите пароль"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Подтверждение email через отсылку почты
    def save(self, commit=True) -> User:
        user = super().save(commit=True)

        if settings.EMAIL_VERIFICATION:
            if settings.CELERY_SWITCH is True:
                send_email_verification.delay(user.id)
            else:
                expiration = now() + timedelta(hours=48)
                record = EmailVerification.objects.create(
                    code=uuid.uuid4(), user=user, expiration=expiration
                )
                record.send_verification_email()
        return user


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4"})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "image", "email", "username")
