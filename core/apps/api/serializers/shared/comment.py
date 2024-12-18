from rest_framework import serializers

from ...models import CommentModel
from ..user import ListUserSerializer
from core.utils.cache import Cache


class BaseCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = ListUserSerializer()

    def __get_replies(self, obj):
        if obj.replies.exists():
            return ListCommentSerializer(obj.replies.all(), many=True).data
        return []

    def get_replies(self, obj):
        return Cache().remember(self.__get_replies, key="comment_replies_%s" % obj.id, timeout=1200, obj=obj)

    class Meta:
        model = CommentModel
        exclude = [
            "created_at",
            "updated_at",
            "parent",
            "content",
        ]


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
