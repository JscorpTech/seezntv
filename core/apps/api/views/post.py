from typing import Any

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import PostModel
from ..serializers.post import CreatePostSerializer, ListPostSerializer, RetrievePostSerializer
from drf_spectacular.utils import extend_schema
from django_core.mixins import BaseViewSetMixin


@extend_schema(tags=["post"], deprecated=True)
class PostView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PostModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListPostSerializer
            case "retrieve":
                return RetrievePostSerializer
            case "create":
                return CreatePostSerializer
            case _:
                return ListPostSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
