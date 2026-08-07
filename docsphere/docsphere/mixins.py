from .permissions import IsSubscriptionActive


class ActiveSubscriptionMixin:
    """
    Mixin to strictly require an active organization subscription for accessing the ViewSet.
    """

    def get_permissions(self):
        permissions = super().get_permissions()

        permissions.append(IsSubscriptionActive())

        return permissions
