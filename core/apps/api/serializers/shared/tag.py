from rest_framework import serializers

from ...models import TagModel


class BaseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        exclude = []


class ListTagSerializer(BaseTagSerializer):
    class Meta(BaseTagSerializer.Meta): ...


class RetrieveTagSerializer(BaseTagSerializer):
    class Meta(BaseTagSerializer.Meta): ...


class CreateTagSerializer(BaseTagSerializer):
    class Meta(BaseTagSerializer.Meta): ...
