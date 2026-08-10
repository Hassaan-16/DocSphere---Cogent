from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id",
            "username",
            "email",
            "full_name",
            "org",
            "is_active",
            "is_staff",
            "created_at",
        ]

        read_only_fields = ["user_id", "created_at"]
