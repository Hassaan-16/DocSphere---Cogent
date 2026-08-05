from django.contrib import admin
from .models import (
    Organization,
    User,
    UserCredentialInvite,
    OrganizationSubscription,
    Project,
    Document,
    ProjectShare,
    DocumentShare,
)

admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Document)
admin.site.register(ProjectShare)
admin.site.register(DocumentShare)
admin.site.register(UserCredentialInvite)
admin.site.register(OrganizationSubscription)
