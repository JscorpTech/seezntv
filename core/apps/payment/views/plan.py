from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import PlanModel
from ..serializers.plan import CreatePlanSerializer, ListPlanSerializer, RetrievePlanSerializer


@extend_schema(tags=["plan"])
class PlanView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PlanModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListPlanSerializer
            case "retrieve":
                return RetrievePlanSerializer
            case "create":
                return CreatePlanSerializer
            case _:
                return ListPlanSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
