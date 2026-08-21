USER_FIELDS = [
    "id",
    "username",
    "email",
    "full_name",
    "org",
    "is_active",
    "is_staff",
    "created_at",
    "updated_at",
]

USER_READ_ONLY_FIELDS = ["id", "created_at", "updated_at"]

USER_NAME = "username"

REQUIRED_USER_FIELDS = ["email", "full_name"]

INVITATION = "invitation"

SENT_INVITATION = "sent_invitations"

IS_STAFF = "is_staff"

IS_SUPERUSER = "is_superuser"
