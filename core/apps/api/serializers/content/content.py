from rest_framework import serializers

from ...models import ContentModel


class BaseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModel
        exclude = []


class ListContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta): ...


class RetrieveContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta): ...


class CreateContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta): ...
