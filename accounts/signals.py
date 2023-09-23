from django.conf import settings
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import UserActivateTokens
from django.utils.timezone import make_aware

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def publish_activate_token(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        user_activate_token = UserActivateTokens.objects.create(
            user=instance,
            expired_at=make_aware(datetime.now()) + timedelta(hours=settings.ACTIVATION_EXPIRED_HOURS),
        )
        subject = "メールアドレスを確認してください - 暁の人狼"
        message = f"以下のリンクにアクセスしてメールアドレスを確認してください。\n https://{settings.DOMAIN}/account/activation/{user_activate_token.activate_token}/\n\n 心当たりのない方は、このメールを無視してください。"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [
            instance.email,
        ]
        send_mail(subject, message, from_email, recipient_list)