from rest_framework import serializers

from core.apps.content.models.break_items import Break


class BreaksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Break
        fields = "__all__"
        depth = 2
