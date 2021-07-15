from django.conf import settings
from django.core.mail import EmailMessage


def create_email(subject, body, to, cc=None, bcc=settings.ADMINISTRATOR_EMAILS, from_email=None, html=False):
    email = EmailMessage(
        subject=subject,
        body=body,
        to=to,
        from_email=from_email,
        cc=cc,
        bcc=bcc
    )
    if html:
        email.content_subtype = "html"
    return email
