from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from django.urls import reverse, reverse_lazy
from rest_framework.test import APIClient, APITestCase

from files.models import File
from users.models import User


class HabitTest(APITestCase):
    def setUp(self):
        """ Создание пользователя в тесте и его авторизация"""
        self.client = APIClient()
        self.user = User.objects.create(
            id=1,
            email="admin@admin.admin",
            password="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        self.user.set_password("admin")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_file(self):
        """ Создание файла """
        file = SimpleUploadedFile('file.txt', b'file')
        data = {
            "title": "Новый файл",
            "file": file,
            "user": self.user.pk
        }

        response = self.client.post(reverse('files:create_file'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(File.objects.filter(title=data['title']).exists())

    def test_update_file(self):
        """ Обновление файла """

        file = SimpleUploadedFile('file.txt', b'file')
        data = {
            "title": "Новый файл",
            "file": file,
            "user": self.user.pk
        }
        self.client.post(reverse('files:create_file'), data=data)
        file_pk = File.objects.first().pk

        data2 = {
            "title": "test1"
        }
        response = self.client.patch(reverse('files:update_file', args=[file_pk]), data2)
        self.assertTrue(File.objects.filter(title=data2['title']).exists())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_file(self):
        """ Удаление файла """

        file = SimpleUploadedFile('file.txt', b'file')
        data = {
            "title": "Новый файл",
            "file": file,
            "user": self.user.pk
        }
        self.client.post(reverse('files:create_file'), data=data)
        file_pk = File.objects.first().pk

        delete_url = reverse('files:delete_file', args=[file_pk])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_file(self):
        """ Тест детального просмотра привычки """

        file = SimpleUploadedFile('file.txt', b'file')
        data = {
            "title": "Новый файл",
            "file": file,
            "user": self.user.pk
        }
        self.client.post(reverse('files:create_file'), data=data)

        file_pk = File.objects.first().pk

        response = self.client.get(reverse('files:detail_file', args=[file_pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_file(self):
        """ Просмотр всех файлов """

        file = SimpleUploadedFile('file.txt', b'file')
        file2 = SimpleUploadedFile('file2.txt', b'file')
        data = {
            "title": "Новый файл",
            "file": file,
            "user": self.user.pk
        }

        data2 = {
            "title": "Новый",
            "file": file2,
            "user": self.user.pk
        }

        self.client.post(reverse('files:create_file'), data)
        self.client.post(reverse('files:create_file'), data2)

        response = self.client.get(reverse('files:list_files'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(File.objects.all().count(), 2)
