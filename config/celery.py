from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': {
        'task': 'files.tasks.send_mail_user_task',
        'schedule': timedelta(seconds=5),
    },
}
