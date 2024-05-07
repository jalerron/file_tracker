from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """проверка на владельца"""
    def has_object_permission(self, request, view, obj):
        return request.user.username == obj.username
