from django.urls import path

from files.apps import FilesConfig
from files.views import FileListAPIView, FileCreateAPIView, FileUpdateAPIView, FileDeleteAPIView, FileDetailAPIView

app_name = FilesConfig.name

urlpatterns = [
    path('list/', FileListAPIView.as_view(), name='list_files'),
    path('create/', FileCreateAPIView.as_view(), name='create_file'),
    path('update/<int:pk>/', FileUpdateAPIView.as_view(), name='update_file'),
    path('delete/<int:pk>/', FileDeleteAPIView.as_view(), name='delete_file'),
    path('detail/<int:pk>/', FileDetailAPIView.as_view(), name='detail_file'),

]