"""API views for organizations."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Organization
from .serializers import (
    OrganizationSerializer,
    OrganizationSubscriptionSerializer,
)
from .mixins import ActiveSubscriptionMixin


class OrganizationViewSet(viewsets.ModelViewSet):
    """ViewSet for managing organizations."""

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class OrganizationSubscriptionViewSet(ActiveSubscriptionMixin, viewsets.ModelViewSet):
    """ViewSet for viewing organization subscription details."""

    serializer_class = OrganizationSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return organizations filtered by the requesting user's organization."""
        return Organization.objects.filter(id=self.request.user.org_id)
