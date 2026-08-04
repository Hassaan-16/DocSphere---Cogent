from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    UserManager,
)

class Organization(models.Model):
    org_id = models.BigAutoField(primary_key=True)
    org_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='users'
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'org']

    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} ({self.username})"


class UserCredentialInvite(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('EXPIRED', 'Expired'),
    ]

    invite_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='invites'
    )
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='invite'
    )
    invite_token = models.CharField(max_length=255, unique=True)
    invite_status = models.CharField(
        max_length=50, 
        choices=STATUS_CHOICES, 
        default='PENDING'
    )
    accepted_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite {self.invite_token} for {self.user.email}"


class OrganizationSubscription(models.Model):
    stripe_subscription = models.OneToOneField(
        'djstripe.Subscription', 
        on_delete=models.CASCADE, 
        to_field='id', 
        primary_key=True,
        db_column='stripe_subscription_id'
    )
    org = models.OneToOneField(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='subscription'
    )

    def __str__(self):
        return str(self.pk)


class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='projects'
    )
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='created_projects'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Document(models.Model):
    document_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='documents'
    )
    document_title = models.CharField(max_length=255)
    content_text = models.TextField(blank=True, null=True)
    created_by_user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='created_documents'
    )
    last_updated_by_user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='updated_documents'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.document_title


class ProjectShare(models.Model):
    PERMISSION_CHOICES = [
        ('VIEWER', 'Viewer'),
        ('EDITOR', 'Editor'),
        ('ADMIN', 'Admin'),
    ]

    project_share_id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='shares'
    )
    grantee_user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='project_shares'
    )
    permission_level = models.CharField(
        max_length=50, 
        choices=PERMISSION_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grantee_user.username} - {self.project.project_name} ({self.permission_level})"


class DocumentShare(models.Model):
    PERMISSION_CHOICES = [
        ('VIEWER', 'Viewer'),
        ('EDITOR', 'Editor'),
    ]

    document_share_id = models.BigAutoField(primary_key=True)
    document = models.ForeignKey(
        Document, 
        on_delete=models.CASCADE, 
        related_name='shares'
    )
    grantee_user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='document_shares'
    )
    permission_level = models.CharField(
        max_length=50, 
        choices=PERMISSION_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grantee_user.username} - {self.document.document_title} ({self.permission_level})"
        