"""Organization models."""

from djstripe.models import Customer
from django.db import models

from core.models.abstract import TimeStampedModel


class Organization(TimeStampedModel):
    """Represents an organization within the system."""

    org_name = models.CharField(max_length=255)
    stripe_customer_id = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )

    @property
    def active_subscription(self):
        """Return the active djstripe Subscription for this organization."""
        if not self.stripe_customer_id:
            return None

        try:
            customer = Customer.objects.get(id=self.stripe_customer_id)
            return (
                customer.subscriptions.filter(status="active")
                .select_related("plan__product")
                .first()
            )

        except Customer.DoesNotExist:
            return None

    @property
    def subscription_status(self):
        """Return the status of the active subscription."""
        sub = self.active_subscription
        return sub.status if sub else None

    @property
    def current_plan_name(self):
        """Return the name of the current subscription plan."""
        sub = self.active_subscription
        return sub.plan.product.name if sub and sub.plan else None

    @property
    def current_period_end(self):
        """Return the end date of the current subscription period."""
        sub = self.active_subscription
        return sub.current_period_end if sub else None

    def __str__(self):
        """Return the organization name."""
        return self.org_name
