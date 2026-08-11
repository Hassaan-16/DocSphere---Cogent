from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self, username, email, full_name, org, password=None, **extra_fields
    ):
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
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(
            username, email, full_name, org, password, **extra_fields
        )
