from rest_framework import serializers

from core.apps.content.models.break_items import BreakList


class BreaksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakList
        fields = "__all__"
        depth = 2
