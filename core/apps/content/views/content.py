import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny

from core.apps.content.models import Content, Genre, Category
from django.db.models import Prefetch
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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ContentFilter

    def get_queryset(self) -> generics.QuerySet:
        return (
            Content.objects.all()
            .prefetch_related(
                Prefetch("genre", queryset=Genre.objects.all()),
                Prefetch("category", queryset=Category.objects.all()),
            )
            .order_by("-id")
        )

    permission_classes = [AllowAny]


class ContentRetrieve(generics.RetrieveAPIView):

    queryset = Content.objects.all()
    serializer_class = ContentRetriveSerializer

    permission_classes = [AllowAny]
