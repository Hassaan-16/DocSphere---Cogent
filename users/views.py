from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for viewing and managing User accounts.
    Optimizes queries by pre-fetching the related Organization data.
    """

    queryset = User.objects.select_related("org").all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
