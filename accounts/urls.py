from django.urls import path
from . import views
import uuid

app_name = "accounts"

urlpatterns = [
    path("signup/", views.Signup.as_view(), name="signup"),
    path("signup_email/", views.Signup_email.as_view(), name="signup_email"),
    path("activation/<uuid:activate_token>/", views.signup_complete, name="signup_complete"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
]