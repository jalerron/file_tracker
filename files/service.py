from django.core.mail import send_mail

from config import settings
from files.models import File


def send_mail_users(emails: list, subject_, message_):
    send_mail(
        subject=subject_,
        message=message_,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails,
        fail_silently=False,
    )


def check_status():
    objs = File.objects.all()
    for obj in objs:

        if obj.status == 'CONFIRMED' and not obj.is_send:
            email = [obj.user.email]
            subject_ = 'Файл подтвержден!'
            message_ = f'Ваш файл был подтвержден.'
            obj.is_send = True
            obj.save()
            send_mail_users(email, subject_, message_)

        if obj.status == 'REJECTED' and not obj.is_send:
            email = [obj.user.email]
            subject_ = 'Файл отклонен!'
            message_ = f'Ваш файл был отклонен.'
            obj.is_send = True
            obj.save()
            send_mail_users(email, subject_, message_)
