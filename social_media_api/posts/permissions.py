from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Allow read access to everyone,
    but only allow owners to edit/delete.
    """

    def has_object_permission(self, request, view, obj):

        # Allow GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user