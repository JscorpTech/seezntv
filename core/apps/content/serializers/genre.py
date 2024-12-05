from rest_framework import serializers

from core.apps.content.models.genre import GenreList


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreList
        fields = "__all__"
        depth = 1
