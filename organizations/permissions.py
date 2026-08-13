"""Custom permissions for organization-based access control."""

from .constants import ACTIVE_STATE, ORGANIZATION_ABBR
from rest_framework import permissions


class IsSubscriptionActive(permissions.BasePermission):
    """Allow access only if user's organization has an active subscription."""

    message = "Your organization's subscription is inactive or expired."

    def has_permission(self, request, view):
        """Check if the requesting user's organization has an active subscription."""
        if request.user.is_superuser:
            return True

        if not hasattr(request.user, ORGANIZATION_ABBR) or not request.user.org:
            return False

        return request.user.org.subscription_status == ACTIVE_STATE
