"""API views for projects."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project, ProjectShare
from .serializers import ProjectSerializer, ProjectShareSerializer
from organizations.mixins import ActiveSubscriptionMixin


class ProjectViewSet(ActiveSubscriptionMixin, viewsets.ModelViewSet):
    """ViewSet for managing projects."""

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return projects filtered by the requesting user's organization."""
        return Project.objects.filter(org=self.request.user.org).select_related(
            "org", "created_by_user"
        )

    def perform_create(self, serializer):
        """Save project with current user's organization and as creator."""
        serializer.save(org=self.request.user.org, created_by_user=self.request.user)


class ProjectShareViewSet(ActiveSubscriptionMixin, viewsets.ModelViewSet):
    """ViewSet for managing project shares."""

    serializer_class = ProjectShareSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return project shares filtered by the requesting user's organization."""
        return ProjectShare.objects.filter(
            project__org=self.request.user.org
        ).select_related("project", "grantee_user", "granted_by")
