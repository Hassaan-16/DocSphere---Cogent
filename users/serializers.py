"""Serializers for users."""

from rest_framework import serializers

from .constants import (
    USER_FIELDS,
    USER_READ_ONLY_FIELDS,
)
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = [USER_FIELDS]
        read_only_fields = [USER_READ_ONLY_FIELDS]
