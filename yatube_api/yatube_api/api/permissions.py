from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Только владельцам объекта может редактировать его его."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
