"""Factory for creating superusers."""

from django.apps import apps

from .organization_resolver import OrganizationResolver


class SuperuserFactory:
    """Create superusers with default organization."""

    DEFAULT_ORG_NAME = "Admin HQ"

    @classmethod
    def create(cls, username, email, full_name, password=None, **extra_fields):
        """Create a superuser assigned to the default Admin HQ organization."""
        org = OrganizationResolver.resolve(cls.DEFAULT_ORG_NAME)
        User = apps.get_model("users", "User")

        return User.objects.create_superuser(
            username, email, full_name, org, password, **extra_fields
        )
