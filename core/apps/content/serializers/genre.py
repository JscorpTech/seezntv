from rest_framework import serializers

from core.apps.content.models.genre import Genre


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        depth = 1
