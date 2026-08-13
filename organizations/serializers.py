"""Serializers for organizations."""

from rest_framework import serializers

from .constants import (
    ORGANIZATION_FIELDS,
    ORGANIZATION_READ_ONLY_FIELDS,
    ORGANIZATION_SUBSCRIPTION_FIELDS,
    ORGANIZATION_SUBSCRIPTION_READ_ONLY_FIELDS,
)
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
        fields = [ORGANIZATION_FIELDS]
        read_only_fields = [ORGANIZATION_READ_ONLY_FIELDS]


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
        fields = [ORGANIZATION_SUBSCRIPTION_FIELDS]
        read_only_fields = [ORGANIZATION_SUBSCRIPTION_READ_ONLY_FIELDS]
