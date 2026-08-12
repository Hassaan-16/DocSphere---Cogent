"""Abstract base models for the project."""

from django.db import models


class TimeStampedModel(models.Model):
    """Abstract model providing created_at and updated_at timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class OrganizationOwnedModel(models.Model):
    """Abstract model for models owned by an Organization."""

    org = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="%(class)s_set",
    )

    class Meta:
        abstract = True
