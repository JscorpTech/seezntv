from rest_framework import serializers

from ...models import CadrModel


class BaseCadrSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadrModel
        exclude = [
            "created_at",
            "updated_at"
        ]


class ListCadrSerializer(BaseCadrSerializer):
    class Meta(BaseCadrSerializer.Meta): ...


class RetrieveCadrSerializer(BaseCadrSerializer):
    class Meta(BaseCadrSerializer.Meta): ...


class CreateCadrSerializer(BaseCadrSerializer):
    class Meta(BaseCadrSerializer.Meta): ...
