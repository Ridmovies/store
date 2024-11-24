from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')