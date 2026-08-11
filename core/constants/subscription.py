from django.db import models


class SubscriptionStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    PAST_DUE = "past_due", "Past Due"
    CANCELED = "canceled", "Canceled"
    TRIALING = "trialing", "Trialing"
    INCOMPLETE = "incomplete", "Incomplete"
    INCOMPLETE_EXPIRED = "incomplete_expired", "Incomplete Expired"
    UNPAID = "unpaid", "Unpaid"
    PAUSED = "paused", "Paused"
