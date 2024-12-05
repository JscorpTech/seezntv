from rest_framework import serializers

from ...models import MediaModel
from config.env import env


class BaseMediaSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        return "%s//%s/%s" % (env.str("STORAGE_PROTOCOL"), env.str("STORAGE_PATH"), obj.video)

    class Meta:
        model = MediaModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListMediaSerializer(BaseMediaSerializer):
    class Meta(BaseMediaSerializer.Meta): ...


class RetrieveMediaSerializer(BaseMediaSerializer):
    class Meta(BaseMediaSerializer.Meta): ...


class CreateMediaSerializer(BaseMediaSerializer):
    class Meta(BaseMediaSerializer.Meta): ...
