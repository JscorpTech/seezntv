from typing import Any

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ContentModel
from ..serializers.content import (CreateContentSerializer,
                                   ListContentSerializer,
                                   RetrieveContentSerializer)


class ContentView(ReadOnlyModelViewSet):
    queryset = ContentModel.objects.all()

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
