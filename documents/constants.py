DOCUMENT_FIELDS = [
    "id",
    "project",
    "document_title",
    "content_text",
    "created_by_user",
    "last_updated_by_user",
    "created_at",
    "updated_at",
]

DOCUMENT_READ_ONLY_FIELDS = [
    "id",
    "created_by_user",
    "last_updated_by_user",
    "created_at",
    "updated_at",
]

DOCUMENT_SHARE_FIELDS = [
    "id",
    "document",
    "grantee_user",
    "permission_level",
    "granted_by",
    "created_at",
    "updated_at",
]

DOCUMENT_SHARE_READ_ONLY_FIELDS = ["id", "granted_by", "created_at", "updated_at"]
