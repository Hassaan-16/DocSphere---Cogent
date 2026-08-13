PROJECT_FIELDS = [
    "id",
    "project_name",
    "description",
    "org",
    "created_by_user",
    "created_at",
    "updated_at",
]

PROJECT_READ_ONLY_FIELDS = ["id", "org", "created_by_user", "created_at", "updated_at"]

PROJECT_SHARE_FIELDS = [
    "id",
    "project",
    "grantee_user",
    "permission_level",
    "granted_by",
    "created_at",
    "updated_at",
]

PROJECT_SHARE_READ_ONLY_FIELDS = ["id", "granted_by", "created_at", "updated_at"]
