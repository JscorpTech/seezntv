from rest_framework import serializers

from ...models import ContentModel
from ..shared import ListTagSerializer, ListGenreSerializer, ListCategorySerializer, ListCadrSerializer
from ..media import ListMediaSerializer


class BaseContentSerializer(serializers.ModelSerializer):
    genre = ListGenreSerializer(many=True)
    tags = ListTagSerializer(many=True)
    category = ListCategorySerializer(many=True)
    contents = ListMediaSerializer(many=True)
    ova = ListMediaSerializer(many=True)
    chronology = ListMediaSerializer(many=True)
    cadrs = ListCadrSerializer(many=True)

    class Meta:
        model = ContentModel
        exclude = [
            "created_at",
            "updated_at",
            "title_uz",
            "title_en",
            "title_ru",
            "description_uz",
            "description_en",
            "description_ru",
        ]
        depth = 1


class ListContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta):
        exclude = None
        fields = [
            "id",
            "title",
            "genre",
            "tags",
            "poster_desktop",
            "poster_mobile",
            "poster_card",
            "poster_video",
            "created_at",
        ]


class RetrieveContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta): ...


class CreateContentSerializer(BaseContentSerializer):
    class Meta(BaseContentSerializer.Meta): ...
