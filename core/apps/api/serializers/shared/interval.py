from rest_framework import serializers

from ...models import IntervalModel


class BaseIntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalModel
        exclude = []


class ListIntervalSerializer(BaseIntervalSerializer):
    class Meta(BaseIntervalSerializer.Meta): ...


class RetrieveIntervalSerializer(BaseIntervalSerializer):
    class Meta(BaseIntervalSerializer.Meta): ...


class CreateIntervalSerializer(BaseIntervalSerializer):
    class Meta(BaseIntervalSerializer.Meta): ...
