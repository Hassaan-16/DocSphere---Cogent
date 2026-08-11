from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization, OrganizationSubscription
from .serializers import (
    OrganizationSerializer,
    OrganizationSubscriptionSerializer,
)


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API ViewSet allowing authenticated users to view or edit Organization data.
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OrganizationSubscriptionViewSet(viewsets.ModelViewSet):
    """
    API ViewSet allowing authenticated users to view their specific
    Organization's billing and subscription status.
    """

    serializer_class = OrganizationSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filters the queryset to securely return only the subscription
        tied to the requesting user's organization.
        """

        return OrganizationSubscription.objects.filter(
            org=self.request.user.org
        ).select_related("org", "stripe_subscription")
