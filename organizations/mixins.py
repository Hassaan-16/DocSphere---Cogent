"""View mixins for organization-based access control."""

from .permissions import IsSubscriptionActive


class ActiveSubscriptionMixin:
    """View mixin to require an active organization subscription."""

    def get_permissions(self):
        """Append IsSubscriptionActive permission to the view's existing permissions."""
        permissions = super().get_permissions()
        permissions.append(IsSubscriptionActive())

        return permissions
