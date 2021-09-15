"""User permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from users.models import User


class IsStandardUser(BasePermission):
    """Allow access to create posts."""

    def has_permission(self, request, view):

        try:
            user = User.objects.get(
                email=request.user,
                is_staff=False
            )
        except User.DoesNotExist:
            return False
        return True