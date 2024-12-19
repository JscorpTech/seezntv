from rest_framework import serializers

from ...models import CadrModel
from core.utils import Url


class BaseCadrSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return Url.unquote_if_exists(
            super().to_representation(instance),
            [
                "image",
            ],
        )

    class Meta:
        model = CadrModel
        exclude = [
            "created_at",
            "updated_at",
            "content",
        ]


class ListCadrSerializer(BaseCadrSerializer):
    class Meta(BaseCadrSerializer.Meta): ...


class RetrieveCadrSerializer(BaseCadrSerializer):
    class Meta(BaseCadrSerializer.Meta): ...


class CreateCadrSerializer(BaseCadrSerializer):
    class Meta(BaseCadrSerializer.Meta): ...
