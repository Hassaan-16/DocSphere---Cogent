"""API views for users."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for managing users."""

    queryset = User.objects.select_related("org").all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
