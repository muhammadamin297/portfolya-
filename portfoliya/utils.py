from django.core.mail import send_mail
from django.conf import settings

def send_verification_code(email, code):
    subject = "Ro'yxatdan o'tish kodi"
    message = f"Sizning tasdiqlash kodingiz: {code}"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])
