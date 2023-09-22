from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.core.mail import send_mail

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("ユーザー名"),
        max_length=16,
        help_text=_("必須。16文字以内。半角英数字と@/./+/-/_のみ。"),
        validators=[username_validator],
        unique=True,
        error_messages={
            "unique":_("そのユーザー名は既に使用されています。"),
        },
    )
    email = models.EmailField(_("メールアドレス"), unique=True)
    is_staff = models.BooleanField(
        _("管理者"),
        default=False,
    )
    is_active = models.BooleanField(
        _("有効"),
        default=True,
    )
    date_joined = models.DateTimeField(_("登録日時"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("ユーザー")
        verbose_name_plural = _("ユーザー")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        # このユーザーにメールを送る
        send_mail(subject, message, from_email, [self.email], **kwargs)