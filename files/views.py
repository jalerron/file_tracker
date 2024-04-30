from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from config import settings
from files.models import File
from files.permisions import IsOwner
from files.serializers import FileSerializer
from files.tasks import send_mail_admins_task


class FileListAPIView(generics.ListAPIView):
    """ Вывод списка файлов """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]


class FileCreateAPIView(generics.CreateAPIView):
    """ Создание файла """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        file = serializer.save()
        file.user = self.request.user
        file.save()
        subject = "Новый файл"
        message = f"На портал был загужен новый файл пользователем {file.user.username}"
        send_mail_admins_task.delay(subject, message)


class FileDetailAPIView(generics.RetrieveAPIView):
    """ Детальный обзор файлв """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]


class FileUpdateAPIView(generics.RetrieveUpdateAPIView):
    """ Обновление файла """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        file = serializer.save()
        file.is_send = False
        file.status = "NONE"
        file.save()
        subject = "Файл был обновлен"
        message = f"Файл был обновлен пользователем {file.user.username}"
        send_mail_admins_task.delay(subject, message)


class FileDeleteAPIView(generics.RetrieveDestroyAPIView):
    """ Удаление файла """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAdminUser | IsOwner]
