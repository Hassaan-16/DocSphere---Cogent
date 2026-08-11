from django.db import models


class InvitationStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    EXPIRED = "EXPIRED", "Expired"
    REVOKED = "REVOKED", "Revoked"
