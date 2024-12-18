from typing import Any

from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django_core.paginations import CustomPagination
from django_core.mixins import BaseViewSetMixin
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
from django.db import models


@extend_schema(tags=["category"])
class CategoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.order_by("position").all()
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
class GenreView(BaseViewSetMixin, ReadOnlyModelViewSet):
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
class TagView(BaseViewSetMixin, ReadOnlyModelViewSet):
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
class IntervalView(BaseViewSetMixin, ReadOnlyModelViewSet):
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
class CommentView(BaseViewSetMixin, CreateModelMixin, GenericViewSet):
    queryset = CommentModel.objects.order_by("-created_at").all()

    @extend_schema(responses={200: ListCommentSerializer(many=True)})
    def retrieve(self, request, pk):
        paginator = CustomPagination()
        only_fields = (
            "user__first_name",
            "user__last_name",
            "user__id",
            "user__username",
            "parent",
            "id",
            "text",
        )
        queryset = (
            CommentModel.objects.filter(content_id=pk, parent__isnull=True)
            .select_related("user")
            .prefetch_related(
                models.Prefetch("replies", CommentModel.objects.order_by("-created_at").only(*only_fields))
            )
            .only(*only_fields)
            .order_by("-created_at")
            .all()
        )
        queryset = paginator.paginate_queryset(queryset, request)
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
