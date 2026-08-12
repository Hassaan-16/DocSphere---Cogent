"""Serializers for organizations."""

from rest_framework import serializers

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for the Organization model."""

    subscription_status = serializers.CharField(
        source="subscription_status", read_only=True
    )
    current_plan_name = serializers.CharField(
        source="current_plan_name", read_only=True
    )
    current_period_end = serializers.DateTimeField(
        source="current_period_end", read_only=True
    )

    class Meta:
        model = Organization
        fields = [
            "id",
            "org_name",
            "created_at",
            "updated_at",
            "subscription_status",
            "current_plan_name",
            "current_period_end",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class OrganizationSubscriptionSerializer(serializers.ModelSerializer):
    """Serializer for organization subscription details."""

    subscription_status = serializers.CharField(
        source="subscription_status", read_only=True
    )
    current_plan_name = serializers.CharField(
        source="current_plan_name", read_only=True
    )
    current_period_end = serializers.DateTimeField(
        source="current_period_end", read_only=True
    )

    class Meta:
        model = Organization
        fields = [
            "id",
            "org_name",
            "subscription_status",
            "current_plan_name",
            "current_period_end",
        ]
        read_only_fields = ["id", "org_name"]
