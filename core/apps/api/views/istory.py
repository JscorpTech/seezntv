from typing import Any

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import IstoryModel
from ..serializers.istory import CreateIstorySerializer, ListIstorySerializer, RetrieveIstorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["istory"])
class IstoryView(ReadOnlyModelViewSet):
    queryset = IstoryModel.objects.order_by("position").all()
    pagination_class = None

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListIstorySerializer
            case "retrieve":
                return RetrieveIstorySerializer
            case "create":
                return CreateIstorySerializer
            case _:
                return ListIstorySerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
