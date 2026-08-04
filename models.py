from django.db import models

class Organization(models.Model):
    org_id = models.BigAutoField(primary_key=True)
    org_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    org = models.ForeignKey(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='users'
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_org_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"


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
        related_name='invite',
        null=True, 
        blank=True
    )
    invite_token = models.CharField(max_length=255, unique=True)
    invite_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    accepted_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite {self.invite_token} for Org {self.org_id}"


class OrganizationSubscription(models.Model):
    stripe_subscription_id = models.CharField(max_length=255, primary_key=True)
    org = models.OneToOneField(
        Organization, 
        on_delete=models.CASCADE, 
        related_name='subscription'
    )

    def __str__(self):
        return self.stripe_subscription_id


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
    permission_level = models.CharField(max_length=50, choices=PERMISSION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grantee_user.email} - {self.project.project_name} ({self.permission_level})"


class DocumentShare(models.Model):
    PERMISSION_CHOICES = [
        ('VIEWER', 'Viewer'),
        ('EDITOR', 'Editor'),
        ('ADMIN', 'Admin'),
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
    permission_level = models.CharField(max_length=50, choices=PERMISSION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grantee_user.email} - {self.document.document_title} ({self.permission_level})"
    