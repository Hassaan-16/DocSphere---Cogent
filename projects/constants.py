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

CREATED_PROJECTS = "created_projects"

SHARES = "shares"

PROJECT_SHARES = "project_shares"

GRANTED_PROJECT_SHARES = "granted_project_shares"

PROJECT_COMPOSITE_KEY = ["project", "grantee_user"]

PROJECT = "project"

GRANTEE_USER = "grantee_user"

ACCESS_GRANTED_BY = "granted_by"

ORGANIZATION_ABBR = "org"

CREATED_BY_USER = "created_by_user"
