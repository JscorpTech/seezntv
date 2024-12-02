import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.apps.content.models.content import Content
from core.apps.content.serializers.content import ContentListSerializer, ContentRetriveSerializer


class ContentFilter(django_filters.FilterSet):
    genre = django_filters.AllValuesMultipleFilter(field_name="genre__genre__item", lookup_expr="exact")
    category = django_filters.AllValuesMultipleFilter(field_name="category__category__item", lookup_expr="exact")

    class Meta:
        model = Content
        fields = {
            "title": ["icontains"],
            "age_limit": ["gte", "lte"],
            "release_date": ["gte", "lte"],
        }


class ContentListView(generics.ListAPIView):

    serializer_class = ContentListSerializer
    queryset = Content.objects.all().order_by("-id")
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContentFilter

    permission_classes = [AllowAny]


class ContentRetrieve(generics.RetrieveAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentRetriveSerializer

    permission_classes = [AllowAny]
