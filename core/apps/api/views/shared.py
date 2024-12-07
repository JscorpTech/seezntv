from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from core.http.paginations import CustomPagination


from ..models import CategoryModel, CommentModel, GenreModel, IntervalModel, TagModel
from ..serializers.shared import (
    CreateCategorySerializer,
    CreateCommentSerializer,
    CreateGenreSerializer,
    CreateIntervalSerializer,
    CreateTagSerializer,
    ListCategorySerializer,
    ListCommentSerializer,
    ListGenreSerializer,
    ListIntervalSerializer,
    ListTagSerializer,
    RetrieveCategorySerializer,
    RetrieveGenreSerializer,
    RetrieveIntervalSerializer,
    RetrieveTagSerializer,
)


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


@extend_schema(tags=["comment"])
class CommentView(CreateModelMixin, GenericViewSet):
    queryset = CommentModel.objects.order_by("-created_at").all()

    @action(methods=["GET"], detail=True)
    def comments(self, request, pk):
        paginator = CustomPagination()
        queryset = paginator.paginate_queryset(self.get_queryset(), request)
        return paginator.get_paginated_response(self.get_serializer(queryset, many=True).data)

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCommentSerializer
            case "create":
                return CreateCommentSerializer
            case _:
                return ListCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case "create":
                perms.extend([IsAuthenticated])
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
