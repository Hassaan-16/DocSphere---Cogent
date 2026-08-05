from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Organization, User
from .serializers import (
    UserSerializer,
    OrganizationSerializer,
    OrganizationSubscription,
    OrganizationSubscriptionSerializer,
)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related("org").all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class OrganizationSubscriptionViewSet(viewsets.ModelViewSet):
    """
    Allows users to view their Organization's subscription status.
    """

    serializer_class = OrganizationSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrganizationSubscription.objects.filter(
            org=self.request.user.org
        ).select_related("org", "stripe_subscription")
