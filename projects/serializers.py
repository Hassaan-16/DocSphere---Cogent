"""Serializers for projects."""

from rest_framework import serializers

from .models import Project, ProjectShare
from core.constants.permissions import PROJECT_PERMISSIONS


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the Project model."""

    class Meta:
        model = Project
        fields = [
            "id",
            "project_name",
            "description",
            "org",
            "created_by_user",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "org", "created_by_user", "created_at", "updated_at"]


class ProjectShareSerializer(serializers.ModelSerializer):
    """Serializer for the ProjectShare model."""

    permission_level = serializers.ChoiceField(choices=PROJECT_PERMISSIONS)

    class Meta:
        model = ProjectShare
        fields = [
            "id",
            "project",
            "grantee_user",
            "permission_level",
            "granted_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "granted_by", "created_at", "updated_at"]
