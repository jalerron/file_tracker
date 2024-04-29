from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from config import settings
from files.models import File
from files.serializers import FileSerializer
from files.tasks import send_mail_admins_task


class FileListAPIView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]


class FileCreateAPIView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        file = serializer.save()
        file.user = self.request.user
        file.save()
        send_mail_admins_task.delay(file.user.username)


class FileDetailAPIView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]


class FileUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]
