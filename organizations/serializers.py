from rest_framework import serializers
from .models import Organization, OrganizationSubscription


class OrganizationSubscriptionSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="stripe_subscription.status", read_only=True)
    current_period_end = serializers.DateTimeField(
        source="stripe_subscription.current_period_end", read_only=True
    )
    plan_name = serializers.CharField(
        source="stripe_subscription.plan.product.name", read_only=True, default="N/A"
    )

    class Meta:
        model = OrganizationSubscription
        fields = [
            "stripe_subscription",
            "org",
            "status",
            "plan_name",
            "current_period_end",
        ]
        read_only_fields = ["stripe_subscription", "org"]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["org_id", "org_name", "created_at"]
        read_only_fields = ["org_id", "created_at"]
