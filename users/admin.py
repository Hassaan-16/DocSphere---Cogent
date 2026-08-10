from django.contrib import admin
from .models import User, UserCredentialInvite

admin.site.register(User)
admin.site.register(UserCredentialInvite)
