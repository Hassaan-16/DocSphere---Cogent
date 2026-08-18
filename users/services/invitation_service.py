"""Service for managing user invitations."""

import secrets
from datetime import timedelta

from django.utils import timezone

from core.constants.invitations import (
    INVITATION_TOKEN_LENGTH,
    INVITATION_DEFAULT_EXPIRY_DAYS,
)
from ..models import UserInvitation


class InvitationService:
    """Handle invitation token generation and creation."""

    TOKEN_LENGTH = INVITATION_TOKEN_LENGTH
    DEFAULT_EXPIRY_DAYS = INVITATION_DEFAULT_EXPIRY_DAYS

    @classmethod
    def generate_token(cls) -> str:
        """Generate a secure URL-safe invitation token."""
        return secrets.token_urlsafe(cls.TOKEN_LENGTH)

    @classmethod
    def create_invitation(
        cls, user, org, invited_by, expires_in_days=None
    ) -> UserInvitation:
        """Create a new user invitation with generated token."""
        expires_at = timezone.now() + timedelta(
            days=expires_in_days or cls.DEFAULT_EXPIRY_DAYS
        )

        return UserInvitation.objects.create(
            user=user,
            org=org,
            invite_token=cls.generate_token(),
            expires_at=expires_at,
            invited_by=invited_by,
        )
