from rest_framework import serializers

from .models import Roles, User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default=Roles.USER)

    class Meta:
        fields = (
            'confirmation_code',
            'first_name',
            'last_name',
            'username',
            'email',
            'role',
            'bio',
        )
        model = User
        extra_kwargs = {
            'confirmation_code': {'write_only': True},
            'username': {'required': True},
            'email': {'required': True},
        }