from django.contrib import admin
from .models import (
    Organization, User, UserCredentialInvite, 
    OrganizationSubscription, 
    Project, Document, 
    ProjectShare, DocumentShare
)

admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Document)
admin.site.register(ProjectShare)
admin.site.register(DocumentShare)
admin.site.register(UserCredentialInvite)
admin.site.register(OrganizationSubscription)

# from docsphere.models import User, Organization

# org = Organization.objects.get(org_id=1)

# user = User.objects.create_superuser(
#     username='dave',
#     email='dave@docsphere.com',
#     full_name='System dave',
#     org=org,
#     password='123'
# )

# print(f"Superuser '{user.username}' created successfully!")
# exit()
