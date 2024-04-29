from config.celery import app
from files.service import check_status, send_mail_users
from users.models import User


@app.task
def send_mail_user_task():
    check_status()


@app.task
def send_mail_admins_task(obj_author):
    users_email = []
    users = User.objects.filter(is_staff=True, is_active=True)
    for user in users:
        users_email.append(user.email)
    subject_ = 'Новый файл!'
    message_ = f'На портал загружен новый файл от пользователя {obj_author}.'
    send_mail_users(users_email, subject_, message_)
