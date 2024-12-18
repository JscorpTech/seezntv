from rest_framework import serializers
from django.contrib.auth import get_user_model


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
        ]


class ListUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): ...


class RetrieveUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): ...


class CreateUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta): ...
