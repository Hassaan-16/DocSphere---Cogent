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

DOCUMENTS = "documents"

CREATED_DOCUMENTS = "created_documents"

UPDATED_DOCUMENTS = "updated_documents"

SHARES = "shares"

DOCUMENT_SHARES = "document_shares"

GRANTED_DOCUMENT_SHARES = "granted_document_shares"

DOCUMENT_COMPOSITE_KEY = ["document", "grantee_user"]
