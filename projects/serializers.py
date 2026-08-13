"""Serializers for projects."""

from rest_framework import serializers

from .constants import (
    PROJECT_FIELDS,
    PROJECT_READ_ONLY_FIELDS,
    PROJECT_SHARE_FIELDS,
    PROJECT_SHARE_READ_ONLY_FIELDS,
)
from .models import Project, ProjectShare
from core.constants.permissions import PROJECT_PERMISSIONS


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project model."""

    class Meta:
        model = Project
        fields = [PROJECT_FIELDS]
        read_only_fields = [PROJECT_READ_ONLY_FIELDS]


class ProjectShareSerializer(serializers.ModelSerializer):
    """Serializer for the ProjectShare model."""

    permission_level = serializers.ChoiceField(choices=PROJECT_PERMISSIONS)

    class Meta:
        model = ProjectShare
        fields = [PROJECT_SHARE_FIELDS]
        read_only_fields = [PROJECT_SHARE_READ_ONLY_FIELDS]
