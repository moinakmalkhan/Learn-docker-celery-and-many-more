from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

logger = get_task_logger(__name__)


def send_email(name, email, subject, message):

    context = {
        "name": name,
        "message": message,
    }

    email_body = render_to_string("application/email_message.txt", context)

    email = EmailMessage(
        subject,
        email_body,
        settings.EMAIL_HOST_USER,
        [
            email,
        ],
    )
    email.send(fail_silently=False)
    return "Email sent successfully"


@shared_task(bind=True)
def send_email_task(*args, **kwargs):
    logger.info(f'Sending email to {kwargs["email"]}')
    return send_email(**kwargs)
