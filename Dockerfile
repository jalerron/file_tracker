FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /file_tracker

# Копируем зависимости и код приложения
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python manage.py migrate \
    python manage.py create_su
COPY . .


