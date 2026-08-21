"""API views for documents."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Document, DocumentShare
from .serializers import DocumentSerializer, DocumentShareSerializer
from organizations.mixins import ActiveSubscriptionMixin


class DocumentViewSet(ActiveSubscriptionMixin, viewsets.ModelViewSet):
    """ViewSet for managing documents."""

    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return documents filtered by the requesting user's organization."""
        return Document.objects.filter(
            project__org=self.request.user.org
        ).select_related(
            "project", "project__org", "created_by_user", "last_updated_by_user"
        )

    def perform_create(self, serializer):
        """Save document with current user as creator and last updater."""
        project = serializer.validated_data["project"]
        if project.org != self.request.user.org:
            self.permission_denied(
                self.request, message="Project does not belong to your organization"
            )

        serializer.save(
            created_by_user=self.request.user, last_updated_by_user=self.request.user
        )

    def perform_update(self, serializer):
        """Update document with current user as last updater."""
        serializer.save(last_updated_by_user=self.request.user)


class DocumentShareViewSet(ActiveSubscriptionMixin, viewsets.ModelViewSet):
    """ViewSet for managing document shares."""

    serializer_class = DocumentShareSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return document shares filtered by the requesting user's organization."""
        return DocumentShare.objects.filter(
            document__project__org=self.request.user.org
        ).select_related("document", "document__project", "grantee_user", "granted_by")
