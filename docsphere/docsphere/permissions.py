from rest_framework import permissions

class IsSubscriptioinActive(permissions.BasePermission):
    """
    Allows access only if the user's organization has an active Stripe subscription.
    """
    message = "Your organization's subscription is inactive or expired."
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if not hasattr(request.user, 'org') or not request.user.org:
            return False

        try:
            subscription = request.user.org.subscription.stripe_subscription
            return subscription.status == 'active'
        except AttributeError:
            return False
    
