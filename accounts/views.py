from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import Signup
from .models import UserActivateTokens
from django.urls import reverse_lazy

class Signup(CreateView):
    form_class = Signup
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