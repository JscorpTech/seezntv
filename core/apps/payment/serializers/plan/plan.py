from rest_framework import serializers

from ...models import PlanModel


class BasePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListPlanSerializer(BasePlanSerializer):
    class Meta(BasePlanSerializer.Meta): ...


class RetrievePlanSerializer(BasePlanSerializer):
    class Meta(BasePlanSerializer.Meta): ...


class CreatePlanSerializer(BasePlanSerializer):
    class Meta(BasePlanSerializer.Meta): ...
