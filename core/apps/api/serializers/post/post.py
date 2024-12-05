from rest_framework import serializers

from ...models import PostModel


class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListPostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta):
        exclude = BasePostSerializer.Meta.exclude + ["desc"]


class RetrievePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...


class CreatePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...
