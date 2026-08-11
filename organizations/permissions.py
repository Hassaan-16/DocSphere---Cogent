from rest_framework import permissions


class IsSubscriptionActive(permissions.BasePermission):
    """
    Custom DRF permission class that strictly allows access only if
    the requesting user's organization possesses an active Stripe subscription.
    Superusers automatically bypass this check.
    """

    message = "Your organization's subscription is inactive or expired."

    def has_permission(self, request, view):
        """
        Determines whether the incoming request possesses active subscription privileges.
        """
        if request.user.is_superuser:
            return True

        if not hasattr(request.user, "org") or not request.user.org:
            return False

        try:
            subscription = request.user.org.subscription.stripe_subscription
            return subscription.status == "active"

        except AttributeError:
            return False
