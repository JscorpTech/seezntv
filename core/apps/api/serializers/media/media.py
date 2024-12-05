from rest_framework import serializers

from ...models import MediaModel


class BaseMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListMediaSerializer(BaseMediaSerializer):
    class Meta(BaseMediaSerializer.Meta): ...


class RetrieveMediaSerializer(BaseMediaSerializer):
    class Meta(BaseMediaSerializer.Meta): ...


class CreateMediaSerializer(BaseMediaSerializer):
    class Meta(BaseMediaSerializer.Meta): ...
