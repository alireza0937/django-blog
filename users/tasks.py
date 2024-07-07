from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from iconfig import settings


@shared_task
def send_password_reset_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        context = {
            'email': user.email,
            'domain': settings.DOMAIN,
            'site_name': settings.SITE_NAME,
            'uid': uid,
            'user': user,
            'token': token,
            'protocol': 'http',
        }
        subject = render_to_string('registration/password_reset_subject.txt', context)
        subject = ''.join(subject.splitlines())
        email = render_to_string('registration/password_reset_email.html', context)
        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email])
    except User.DoesNotExist:
        pass