from django.conf import settings
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django_boost.models.mixins import LogicalDeletionMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.core.mail import send_mail
import uuid, datetime
from django.utils.timezone import make_aware

class User(AbstractBaseUser, PermissionsMixin, LogicalDeletionMixin):
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
        default=False,
    )
    date_joined = models.DateTimeField(_("登録日時"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("ユーザー")
        verbose_name_plural = _("ユーザー")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        # このユーザーにメールを送る
        send_mail(subject, message, from_email, [self.email], **kwargs)

class UserActivateTokensManager(models.Manager):
    def activate_user_by_token(self, activate_token):
        user_activate_token = self.filter(
            activate_token=activate_token,
            expired_at__gte=make_aware(datetime.datetime.now()),
        ).first()
        if hasattr(user_activate_token, 'user'):
            user = user_activate_token.user
            user.is_active = True
            user.save()
            return user

class UserActivateTokens(models.Model):
    token_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activate_token = models.UUIDField(default=uuid.uuid4)
    expired_at = models.DateTimeField()

    objects = UserActivateTokensManager()