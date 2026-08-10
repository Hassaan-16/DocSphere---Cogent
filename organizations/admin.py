from django.contrib import admin
from .models import Organization, OrganizationSubscription

admin.site.register(Organization)
admin.site.register(OrganizationSubscription)
