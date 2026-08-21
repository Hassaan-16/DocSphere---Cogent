"""User models."""

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.constants.invitations import InvitationStatus
from core.models.abstract import OrganizationOwnedModel, TimeStampedModel

from .constants import (
    USER_NAME,
    REQUIRED_USER_FIELDS,
    INVITATION,
    SENT_INVITATION,
)
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """Custom user model with organization membership."""

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    org = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="users"
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = USER_NAME
    REQUIRED_FIELDS = REQUIRED_USER_FIELDS
    objects = UserManager()

    def __str__(self):
        """Return user's full name and username."""
        return f"{self.full_name} ({self.username})"


class UserInvitation(TimeStampedModel, OrganizationOwnedModel):
    """Invitation sent to a prospective user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name=INVITATION)
    invite_token = models.CharField(max_length=255, unique=True)
    invite_status = models.CharField(
        max_length=20,
        choices=InvitationStatus.choices,
        default=InvitationStatus.PENDING,
    )
    accepted_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name=SENT_INVITATION,
    )

    def __str__(self):
        """Return invitation token and target email."""
        return f"Invitation {self.invite_token} for {self.user.email}"
