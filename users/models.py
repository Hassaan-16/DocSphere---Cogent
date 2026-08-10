from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
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
    REQUIRED_FIELDS = ["email", "full_name", "org"]

    objects = UserManager()

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
