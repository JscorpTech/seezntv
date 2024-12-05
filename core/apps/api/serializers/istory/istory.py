from rest_framework import serializers

from ...models import IstoryModel


class BaseIstorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IstoryModel
        fields = (
            "id",
            "content"
        )


class ListIstorySerializer(BaseIstorySerializer):
    class Meta(BaseIstorySerializer.Meta): ...


class RetrieveIstorySerializer(BaseIstorySerializer):
    class Meta(BaseIstorySerializer.Meta): ...


class CreateIstorySerializer(BaseIstorySerializer):
    class Meta(BaseIstorySerializer.Meta): ...
