from django.db import models


class Organization(models.Model):
    org_id = models.BigAutoField(primary_key=True)
    org_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name


class OrganizationSubscription(models.Model):
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
        return str(self.pk)
