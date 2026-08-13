"""Custom user manager."""

from django.contrib.auth.models import BaseUserManager

from .constants import (
    IS_STAFF,
    IS_SUPERUSER,
)


class UserManager(BaseUserManager):
    """Manager for User model handling user creation."""

    def create_user(
        self, username, email, full_name, org, password=None, **extra_fields
    ):
        """Create and save a regular user."""
        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(
            username=username, email=email, full_name=full_name, org=org, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self, username, email, full_name, org, password=None, **extra_fields
    ):
        """Create and save a superuser."""
        extra_fields.setdefault(IS_STAFF, True)
        extra_fields.setdefault(IS_SUPERUSER, True)

        return self.create_user(
            username, email, full_name, org, password, **extra_fields
        )
