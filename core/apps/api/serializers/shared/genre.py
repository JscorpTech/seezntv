from rest_framework import serializers

from ...models import GenreModel


class BaseGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreModel
        fields = [
            "id",
            "name"
        ]


class ListGenreSerializer(BaseGenreSerializer):
    class Meta(BaseGenreSerializer.Meta): ...


class RetrieveGenreSerializer(BaseGenreSerializer):
    class Meta(BaseGenreSerializer.Meta): ...


class CreateGenreSerializer(BaseGenreSerializer):
    class Meta(BaseGenreSerializer.Meta): ...
