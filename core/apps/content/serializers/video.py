from rest_framework import serializers

from core.apps.content.models.video import VideoContent


class VideoContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = "__all__"
        depth = 1
