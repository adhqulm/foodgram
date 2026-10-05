"""Permissions for the recipes app."""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Allow modification only by the author."""

    def has_object_permission(self, request, view, obj):
        """Check whether the user may modify the object."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
