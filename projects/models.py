from django.db import models
from django.conf import settings


class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        "organizations.Organization", on_delete=models.CASCADE, related_name="projects"
    )
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_projects",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class ProjectShare(models.Model):
    PERMISSION_CHOICES = [
        ("VIEWER", "Viewer"),
        ("EDITOR", "Editor"),
        ("ADMIN", "Admin"),
    ]

    project_share_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="shares"
    )
    grantee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="project_shares",
    )
    permission_level = models.CharField(max_length=50, choices=PERMISSION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grantee_user.username} - {self.project.project_name} ({self.permission_level})"
