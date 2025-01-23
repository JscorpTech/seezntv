from django_filters import rest_framework as filters

from ..models import PlanModel


class PlanFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PlanModel
        fields = ("name",)
