from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.apps import apps


class CustomUserManager(BaseUserManager):
    def create_user(
        self, username, email, full_name, org, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)

        Organization = apps.get_model("organizations", "Organization")

        if isinstance(org, str):
            org_instance, created = Organization.objects.get_or_create(org_name=org)
            org = org_instance
        elif isinstance(org, int):
            org = Organization.objects.get(pk=org)

        user = self.model(
            username=username, email=email, full_name=full_name, org=org, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, email, full_name, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            username,
            email,
            full_name,
            org="Admin HQ",
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="users"
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "full_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.full_name} ({self.username})"


class UserCredentialInvite(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("ACCEPTED", "Accepted"),
        ("EXPIRED", "Expired"),
    ]

    invite_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="invites"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="invite")
    invite_token = models.CharField(max_length=255, unique=True)
    invite_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="PENDING"
    )
    accepted_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite {self.invite_token} for {self.user.email}"
