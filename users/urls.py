from django.urls import path

from users.apps import UsersConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.views import UserCreateAPIView, UserDetailAPIView, UserListAPIView, UserDestroyAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='detail_user'),
    path('list/', UserListAPIView.as_view(), name='list_user'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]