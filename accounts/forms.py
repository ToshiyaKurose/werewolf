from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="有効なメールアドレスを入力してください",
        label="メールアドレス",
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
