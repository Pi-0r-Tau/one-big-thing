import furl
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from one_big_thing.learning import models


def _strip_microseconds(dt):
    if not dt:
        return None
    return dt.replace(microsecond=0, tzinfo=None)


class EmailVerifyTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        email = user.email or ""
        token_timestamp = _strip_microseconds(user.last_token_sent_at)
        return f"{user.pk}{user.password}{timestamp}{email}{token_timestamp}"


class PasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = _strip_microseconds(user.last_login)
        email = user.email or ""
        token_timestamp = _strip_microseconds(user.last_token_sent_at)
        return f"{user.pk}{user.password}{login_timestamp}{timestamp}{email}{token_timestamp}"


EMAIL_VERIFY_TOKEN_GENERATOR = EmailVerifyTokenGenerator()
PASSWORD_RESET_TOKEN_GENERATOR = PasswordResetTokenGenerator()


EMAIL_MAPPING = {
    "email-verification": {
        "from_address": settings.FROM_EMAIL,
        "subject": "One Big Thing: confirm your email address",
        "template_name": "email/verification.txt",
        "url_name": "verify-email",
        "token_generator": EMAIL_VERIFY_TOKEN_GENERATOR,
    },
    "password-reset": {
        "from_address": settings.FROM_EMAIL,
        "subject": "One Big Thing: password reset",
        "template_name": "email/password-reset.txt",
        "url_name": "password-set",
        "token_generator": PASSWORD_RESET_TOKEN_GENERATOR,
    },
    "account-already-exists": {
        "from_address": settings.FROM_EMAIL,
        "subject": "One Big Thing: registration attempt",
        "template_name": "email/account-already-exists.txt",
        "url_name": "password-reset",
    },
    "send-learning-record": {
        "from_address": settings.FROM_EMAIL,
        "subject": "One Big Thing: Your learning record",
        "template_name": "email/send-learning-record.txt",
    },
}


def _send_token_email(user, subject, template_name, from_address, url_name, token_generator):
    user.last_token_sent_at = timezone.now()
    user.save()
    token = token_generator.make_token(user)
    base_url = settings.BASE_URL
    url_path = reverse(url_name)
    url = str(furl.furl(url=base_url, path=url_path, query_params={"code": token, "user_id": str(user.id)}))
    context = dict(user=user, url=url, contact_address=settings.CONTACT_EMAIL)
    body = render_to_string(template_name, context)
    response = send_mail(
        subject=subject,
        message=body,
        from_email=from_address,
        recipient_list=[user.email],
    )
    return response


def _send_normal_email(subject, template_name, from_address, to_address, context):
    body = render_to_string(template_name, context)
    response = send_mail(
        subject=subject,
        message=body,
        from_email=from_address,
        recipient_list=[to_address],
    )
    return response


def send_password_reset_email(user):
    data = EMAIL_MAPPING["password-reset"]
    return _send_token_email(user, **data)


def send_invite_email(user):
    data = EMAIL_MAPPING["invite-user"]
    user.invited_at = timezone.now()
    user.save()
    return _send_token_email(user, **data)


def send_verification_email(user):
    data = EMAIL_MAPPING["email-verification"]
    return _send_token_email(user, **data)


def send_account_already_exists_email(user):
    data = EMAIL_MAPPING["account-already-exists"]
    base_url = settings.BASE_URL
    reset_url = furl.furl(url=base_url)
    reset_url.path.add(data["url_name"])
    reset_url = str(reset_url)
    context = {"contact_address": settings.CONTACT_EMAIL, "url": base_url, "reset_link": reset_url}
    response = _send_normal_email(
        subject=data["subject"],
        template_name=data["template_name"],
        from_address=data["from_address"],
        to_address=user.email,
        context=context,
    )
    return response


def send_learning_record_email(user, email):
    data = EMAIL_MAPPING["send-learning-record"]
    context = {"sending_user": user, "learnings": user.learning_set.all()}
    response = _send_normal_email(
        subject=data["subject"],
        template_name=data["template_name"],
        from_address=data["from_address"],
        to_address=email,
        context=context,
    )
    return response


def verify_token(user_id, token, token_type):
    user = models.User.objects.get(id=user_id)
    result = EMAIL_MAPPING[token_type]["token_generator"].check_token(user, token)
    return result
