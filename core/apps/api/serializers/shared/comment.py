from rest_framework import serializers

from ...models import CommentModel


class BaseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta): ...


class RetrieveCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta): ...


class CreateCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta):
        exclude = None
        fields = [
            "text",
            "content",
        ]
