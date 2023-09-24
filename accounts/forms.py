from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from hcaptcha_field import hCaptchaField
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text="有効なメールアドレスを入力してください。",
        label="メールアドレス",
    )
    hcaptcha = hCaptchaField(label="")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class LoginForm(AuthenticationForm):
    hcaptcha = hCaptchaField(label="")
    class Meta:
        model = User

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        help_text="登録しているメールアドレスをご入力ください。",
        label="メールアドレス",
    )
    hcaptcha = hCaptchaField(label="")
    class Meta:
        model = User
