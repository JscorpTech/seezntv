from django_filters import rest_framework as filters
from ..models import ContentModel


class ContentFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ContentModel
        fields = ("name",)
