from rest_framework import serializers

from ...models import CommentModel


class BaseCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    def get_replies(self, obj):
        if obj.replies.exists():
            return ListCommentSerializer(obj.replies.all(), many=True).data
        return None

    class Meta:
        model = CommentModel
        exclude = ["created_at", "updated_at", "parent"]


class ListCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta): ...


class RetrieveCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta): ...


class CreateCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta):
        exclude = None
        fields = [
            "id",
            "text",
            "content",
            "parent",
        ]
