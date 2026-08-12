"""Project models."""

from django.conf import settings
from django.db import models

from core.constants.permissions import PermissionLevel
from core.models.abstract import OrganizationOwnedModel, TimeStampedModel


class Project(TimeStampedModel, OrganizationOwnedModel):
    """Project container for documents within an organization."""

    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_projects",
    )

    def __str__(self):
        """Return the project name."""
        return self.project_name


class ProjectShare(TimeStampedModel):
    """Share permissions for a project."""

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="shares"
    )
    grantee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_shares",
    )
    permission_level = models.CharField(max_length=20, choices=PermissionLevel.choices)
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="granted_project_shares",
    )

    class Meta:
        unique_together = ["project", "grantee_user"]

    def __str__(self):
        """Return grantee, project name, and permission level."""
        return f"{self.grantee_user.username} - {self.project.project_name} ({self.permission_level})"
