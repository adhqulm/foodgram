"""Разрешения приложения рецептов."""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение на изменение только для автора."""

    def has_object_permission(self, request, view, obj):
        """Проверка прав пользователя на изменение объекта."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
