from rest_framework import serializers

from core.apps.content.models.istory import Istory


class IstorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Istory
        fields = ("videos", "content")
        depth = 2
