from django.urls import path

from files.apps import FilesConfig
from files.views import FileListAPIView, FileCreateAPIView

app_name = FilesConfig.name

urlpatterns = [
    path('list/', FileListAPIView.as_view(), name='list_files'),
    path('create/', FileCreateAPIView.as_view(), name='create_file'),

]