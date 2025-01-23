from rest_framework import serializers
from ...models import OrderModel


class ManualConfirmSerializer(serializers.Serializer):
    file = serializers.FileField()
    order = serializers.PrimaryKeyRelatedField(queryset=OrderModel.objects.all())
