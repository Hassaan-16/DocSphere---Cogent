from django.contrib import admin
from .models import User, UserInvitation

admin.site.register(User)
admin.site.register(UserInvitation)
