from typing import Any

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CategoryModel, GenreModel, IntervalModel, TagModel
from ..serializers.shared import (
    CreateCategorySerializer,
    CreateGenreSerializer,
    CreateIntervalSerializer,
    CreateTagSerializer,
    ListCategorySerializer,
    ListGenreSerializer,
    ListIntervalSerializer,
    ListTagSerializer,
    RetrieveCategorySerializer,
    RetrieveGenreSerializer,
    RetrieveIntervalSerializer,
    RetrieveTagSerializer,
)
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["category"])
class CategoryView(ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    pagination_class = None

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCategorySerializer
            case "retrieve":
                return RetrieveCategorySerializer
            case "create":
                return CreateCategorySerializer
            case _:
                return ListCategorySerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["genre"])
class GenreView(ReadOnlyModelViewSet):
    queryset = GenreModel.objects.all()
    pagination_class = None

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListGenreSerializer
            case "retrieve":
                return RetrieveGenreSerializer
            case "create":
                return CreateGenreSerializer
            case _:
                return ListGenreSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["tag"])
class TagView(ReadOnlyModelViewSet):
    queryset = TagModel.objects.all()
    pagination_class = None

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListTagSerializer
            case "retrieve":
                return RetrieveTagSerializer
            case "create":
                return CreateTagSerializer
            case _:
                return ListTagSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(["interval"])
class IntervalView(ReadOnlyModelViewSet):
    queryset = IntervalModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListIntervalSerializer
            case "retrieve":
                return RetrieveIntervalSerializer
            case "create":
                return CreateIntervalSerializer
            case _:
                return ListIntervalSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
