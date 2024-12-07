from typing import Any

from django.db.models.query import QuerySet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ContentModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from ..serializers.content import CreateContentSerializer, ListContentSerializer, RetrieveContentSerializer
from drf_spectacular.utils import extend_schema
from core.services import FilterService


@extend_schema(tags=["content"], description="Filmlar")
class ContentView(ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = FilterService.get_fields_locale(
        [
            "title",
            "genre__name",
            "tags__name",
            "category__name",
        ]
    )
    filterset_fields = (
        "genre",
        "tags",
        "category",
    )

    def get_queryset(self) -> QuerySet:
        query = ContentModel.objects.all()
        match self.action:
            case "list":
                return query.prefetch_related("genre", "tags")
            case _:
                return query

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListContentSerializer
            case "retrieve":
                return RetrieveContentSerializer
            case "create":
                return CreateContentSerializer
            case _:
                return ListContentSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
