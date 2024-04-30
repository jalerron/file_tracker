from config.celery import app
from files.service import check_status, send_mail_users
from users.models import User


@app.task
def send_mail_user_task():
    """ Проверка статуса загруженных файлов и отправка писем приизменении статуса"""
    check_status()


@app.task
def send_mail_admins_task(subject, message):
    """ Отправка писем админам, если был загружен новый файл"""
    users_email = []
    users = User.objects.filter(is_staff=True, is_active=True)
    for user in users:
        users_email.append(user.email)
    send_mail_users(users_email, subject, message)
