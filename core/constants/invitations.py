"""Invitation status constants."""

from django.db import models

INVITATION_TOKEN_LENGTH = 32
INVITATION_DEFAULT_EXPIRY_DAYS = 7


class InvitationStatus(models.TextChoices):
    """Status choices for user invitations."""

    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    EXPIRED = "EXPIRED", "Expired"
    REVOKED = "REVOKED", "Revoked"
