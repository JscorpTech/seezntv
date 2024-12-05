from rest_framework import serializers

from ...models import IstoryVideoModel


class BaseIstoryvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IstoryVideoModel
        exclude = []


class ListIstoryvideoSerializer(BaseIstoryvideoSerializer):
    class Meta(BaseIstoryvideoSerializer.Meta): ...


class RetrieveIstoryvideoSerializer(BaseIstoryvideoSerializer):
    class Meta(BaseIstoryvideoSerializer.Meta): ...


class CreateIstoryvideoSerializer(BaseIstoryvideoSerializer):
    class Meta(BaseIstoryvideoSerializer.Meta): ...
