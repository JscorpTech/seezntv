from rest_framework import serializers

from ...models import IstoryModel
from .istoryvideo import ListIstoryvideoSerializer


class BaseIstorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IstoryModel
        fields = ("id", "desc", "image")


class ListIstorySerializer(BaseIstorySerializer):
    class Meta(BaseIstorySerializer.Meta): ...


class RetrieveIstorySerializer(BaseIstorySerializer):
    videos = ListIstoryvideoSerializer(many=True)

    class Meta(BaseIstorySerializer.Meta):
        exclude = None
        fields = ("id", "desc", "videos", "image")


class CreateIstorySerializer(BaseIstorySerializer):
    class Meta(BaseIstorySerializer.Meta): ...
