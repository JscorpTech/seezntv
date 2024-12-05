from rest_framework import serializers

from ...models import BannerModel
from ..content import ListContentSerializer


class BaseBannerSerializer(serializers.ModelSerializer):
    film = ListContentSerializer()

    class Meta:
        model = BannerModel
        fields = [
            "content",
            "film",
        ]


class ListBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...


class RetrieveBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...


class CreateBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...
