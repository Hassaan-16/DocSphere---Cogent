"""Serializers for documents."""

from rest_framework import serializers

from core.constants.permissions import DOCUMENT_PERMISSIONS
from .models import Document, DocumentShare


class DocumentSerializer(serializers.ModelSerializer):
    """Serializer for the Document model."""

    class Meta:
        model = Document
        fields = [
            "id",
            "project",
            "document_title",
            "content_text",
            "created_by_user",
            "last_updated_by_user",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_by_user",
            "last_updated_by_user",
            "created_at",
            "updated_at",
        ]


class DocumentShareSerializer(serializers.ModelSerializer):
    """Serializer for the DocumentShare model."""

    permission_level = serializers.ChoiceField(choices=DOCUMENT_PERMISSIONS)

    class Meta:
        model = DocumentShare
        fields = [
            "id",
            "document",
            "grantee_user",
            "permission_level",
            "granted_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "granted_by", "created_at", "updated_at"]
