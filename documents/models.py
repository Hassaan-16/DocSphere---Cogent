"""Document models."""

from django.conf import settings
from django.db import models

from core.constants.permissions import PermissionLevel
from core.models.abstract import TimeStampedModel


class Document(TimeStampedModel):
    """Document belonging to a project."""

    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="documents"
    )
    document_title = models.CharField(max_length=255)
    content_text = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_documents",
    )
    last_updated_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="updated_documents",
    )

    def __str__(self):
        """Return the document title."""
        return self.document_title

    @property
    def org(self):
        """Return the organization via the project."""
        return self.project.org


class DocumentShare(TimeStampedModel):
    """Share permissions for a document."""

    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="shares"
    )
    grantee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="document_shares",
    )
    permission_level = models.CharField(max_length=20, choices=PermissionLevel.choices)
    granted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="granted_document_shares",
    )

    class Meta:
        unique_together = ["document", "grantee_user"]

    def __str__(self):
        """Return grantee, document title, and permission level."""
        return f"{self.grantee_user.username} - {self.document.document_title} ({self.permission_level})"
