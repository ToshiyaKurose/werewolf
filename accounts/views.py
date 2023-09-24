from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import views as auth_views
from .forms import SignupForm, LoginForm, PasswordResetForm
from .models import UserActivateTokens
from django.urls import reverse_lazy

class Signup(CreateView):
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:signup_email")

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class Signup_email(TemplateView):
    template_name = "signup_email.html"

def signup_complete(request, activate_token):
    activated_user = UserActivateTokens.objects.activate_user_by_token(activate_token)
    if hasattr(activated_user, 'is_active'):
        if activated_user.is_active:
            context = {
            "title": "登録完了",
            "message": "メールアドレスは確認されました",
            }
        else:
            context = {
                "title": "エラーが発生しました",
                "message": "認証が失敗しています。管理者に問い合わせてください。",
            }
    else:
        context = {
            "title": "エラーが発生しました",
            "message": "URLが正しくありません。",
        }
    return render(request, "signup_complete.html", context=context)

class Login(auth_views.LoginView):
    template_name = "login.html"
    form_class = LoginForm

class Logout(auth_views.LogoutView):
    template_name = "logout.html"

class PasswordReset(auth_views.PasswordResetView):
    template_name = "password_reset.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy("accounts:password_reset_done")
    email_template_name = "password_reset_email.txt"
    subject_template_name = "password_reset_subject.txt"

class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = "password_reset_sent.html"

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = "password_reset_form.html"
    success_url = reverse_lazy("accounts:password_reset_complete")

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = "password_reset_done.html"