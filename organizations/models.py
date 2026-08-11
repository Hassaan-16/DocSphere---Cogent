from django.db import models


class Organization(models.Model):
    """
    Represents company within the system.
    All users, projects, and subscriptions are linked to an Organization.
    """

    org_id = models.BigAutoField(primary_key=True)
    org_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the string representation of the Organization."""

        return self.org_name


class OrganizationSubscription(models.Model):
    """
    Links an Organization to a Stripe Subscription for billing purposes.
    Maintains a one-to-one relationship with both Organization and djstripe.Subscription.
    """

    stripe_subscription = models.OneToOneField(
        "djstripe.Subscription",
        on_delete=models.CASCADE,
        to_field="id",
        primary_key=True,
        db_column="stripe_subscription_id",
    )
    org = models.OneToOneField(
        Organization, on_delete=models.CASCADE, related_name="subscription"
    )

    def __str__(self):
        """Returns the primary key as the string representation."""

        return str(self.pk)
