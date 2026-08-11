import secrets
from django.utils import timezone
from datetime import timedelta
from ..models import UserInvitation


class InvitationService:
    TOKEN_LENGTH = 32
    DEFAULT_EXPIRY_DAYS = 7

    @classmethod
    def generate_token(cls) -> str:
        return secrets.token_urlsafe(cls.TOKEN_LENGTH)

    @classmethod
    def create_invitation(
        cls, user, org, invited_by, expires_in_days=None
    ) -> UserInvitation:
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
