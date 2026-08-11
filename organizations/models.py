from django.db import models
from core.models.abstract import TimeStampedModel


class Organization(TimeStampedModel):
    org_name = models.CharField(max_length=255)
    stripe_customer = models.OneToOneField(
        "djstripe.Customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="organization",
    )

    @property
    def active_subscription(self):
        if not self.stripe_customer:
            return None
        return (
            self.stripe_customer.subscriptions.filter(status="active")
            .select_related("plan__product")
            .first()
        )

    @property
    def subscription_status(self):
        sub = self.active_subscription
        return sub.status if sub else None

    @property
    def current_plan_name(self):
        sub = self.active_subscription
        return sub.plan.product.name if sub and sub.plan else None

    @property
    def current_period_end(self):
        sub = self.active_subscription
        return sub.current_period_end if sub else None

    def __str__(self):
        return self.org_name
