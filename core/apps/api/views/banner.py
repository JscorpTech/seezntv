from typing import Any

from django.db.models.query import QuerySet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import BannerModel
from ..serializers.banner import CreateBannerSerializer, ListBannerSerializer, RetrieveBannerSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["banner"])
class BannerView(ReadOnlyModelViewSet):
    pagination_class = None

    def get_queryset(self) -> QuerySet:
        return BannerModel.objects.order_by("position").prefetch_related(
            "film__tags",
            "film__genre",
        )

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListBannerSerializer
            case "retrieve":
                return RetrieveBannerSerializer
            case "create":
                return CreateBannerSerializer
            case _:
                return ListBannerSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
