from django.db import models
from django.conf import settings


class Document(models.Model):
    """
    Represents an individual document containing content text.
    Must be nested beneath a parent Project.
    """

    document_id = models.BigAutoField(primary_key=True)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the document's title."""

        return self.document_title


class DocumentShare(models.Model):
    """
    Manages granular access control (Viewer, Editor) granted to
    specific users for an individual Document.
    """

    PERMISSION_CHOICES = [
        ("VIEWER", "Viewer"),
        ("EDITOR", "Editor"),
    ]

    document_share_id = models.BigAutoField(primary_key=True)
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="shares"
    )
    grantee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="document_shares",
    )
    permission_level = models.CharField(max_length=50, choices=PERMISSION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the grantee's username, document title, and permission level."""

        return f"{self.grantee_user.username} - {self.document.document_title} ({self.permission_level})"
