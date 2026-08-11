from django.db import models


class PermissionLevel(models.TextChoices):
    VIEWER = "VIEWER", "Viewer"
    EDITOR = "EDITOR", "Editor"
    ADMIN = "ADMIN", "Admin"


PROJECT_PERMISSIONS = [
    PermissionLevel.VIEWER,
    PermissionLevel.EDITOR,
    PermissionLevel.ADMIN,
]
DOCUMENT_PERMISSIONS = [PermissionLevel.VIEWER, PermissionLevel.EDITOR]
