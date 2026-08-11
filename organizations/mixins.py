from .permissions import IsSubscriptionActive


class ActiveSubscriptionMixin:
    """
    View mixin to strictly require an active organization subscription
    for accessing the inheriting ViewSet or APIView.
    """

    def get_permissions(self):
        """
        Appends the IsSubscriptionActive permission to the view's existing permissions.
        """
        permissions = super().get_permissions()
        permissions.append(IsSubscriptionActive())

        return permissions
