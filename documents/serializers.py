"""Serializers for documents."""

from rest_framework import serializers

from .constants import (
    DOCUMENT_FIELDS,
    DOCUMENT_READ_ONLY_FIELDS,
    DOCUMENT_SHARE_FIELDS,
    DOCUMENT_SHARE_READ_ONLY_FIELDS,
)
from core.constants.permissions import DOCUMENT_PERMISSIONS
from .models import Document, DocumentShare


class DocumentSerializer(serializers.ModelSerializer):
    """Serializer for the Document model."""

    class Meta:
        model = Document
        fields = [DOCUMENT_FIELDS]
        read_only_fields = [DOCUMENT_READ_ONLY_FIELDS]


class DocumentShareSerializer(serializers.ModelSerializer):
    """Serializer for the DocumentShare model."""

    permission_level = serializers.ChoiceField(choices=DOCUMENT_PERMISSIONS)

    class Meta:
        model = DocumentShare
        fields = [DOCUMENT_SHARE_FIELDS]
        read_only_fields = [DOCUMENT_SHARE_READ_ONLY_FIELDS]
